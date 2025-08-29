from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from app.models import Product, ProductQuantity
from .models import Wishlist
from orders.models import Order, OrderItem


@login_required
def wishlist_view(request):
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = None

    wishlist_sizes = request.session.get('wishlist_sizes', {})
    wishlist_quantities = request.session.get('wishlist_quantities', {})  # <-- поправено име

    products_with_sizes = []
    total_price = 0
    if wishlist:
        for key, size in wishlist_sizes.items():
            prod_id = int(key.split('_')[0])
            product = Product.objects.get(id=prod_id)
            quantity = int(wishlist_quantities.get(key, 1))
            products_with_sizes.append({
                'product': product,
                'size': size,
                'quantity': quantity
            })
            total_price += product.price * quantity

    context = {
        'wishlist': wishlist,
        'products_with_sizes': products_with_sizes,
        'total_price': total_price
    }
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def wishlist_add(request, product_id):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        product = get_object_or_404(Product, id=product_id)
        data = json.loads(request.body)
        size = data.get('size', 'Неодредена')
        quantity = int(data.get('quantity', 1))

        wishlist, created = Wishlist.objects.get_or_create(user=request.user)

        # Клучот сега е product_id + size
        key = f"{product.id}_{size}"

        # SIZE
        wishlist_sizes = request.session.get('wishlist_sizes', {})
        wishlist_sizes[key] = size
        request.session['wishlist_sizes'] = wishlist_sizes

        # QUANTITY
        wishlist_quantities = request.session.get('wishlist_quantities', {})
        if key in wishlist_quantities:
            wishlist_quantities[key] += quantity  # ако веќе постои, додај quantity
        else:
            wishlist_quantities[key] = quantity
        request.session['wishlist_quantities'] = wishlist_quantities

        # за да имаме product list во wishlist
        if not wishlist.products.filter(id=product.id).exists():
            wishlist.products.add(product)

        request.session.modified = True

        return JsonResponse({
            'status': 'success',
            'wishlist_count': len(wishlist_sizes)
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


@login_required
def wishlist_remove(request, product_id):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    product = get_object_or_404(Product, id=product_id)

    if wishlist.products.filter(id=product.id).exists():
        wishlist.products.remove(product)

        wishlist_sizes = request.session.get('wishlist_sizes', {})
        if str(product.id) in wishlist_sizes:
            del wishlist_sizes[str(product.id)]
            request.session['wishlist_sizes'] = wishlist_sizes
            request.session.modified = True

    return redirect('wishlist')


@login_required
def create_order(request):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist_sizes = request.session.get('wishlist_sizes', {})

    if not wishlist.products.exists():
        return redirect('wishlist')

    order = Order.objects.create(
        user=request.user,
        first_name=request.user.first_name or "Име",
        last_name=request.user.last_name or "Презиме",
        email=request.user.email or "test@example.com",
        city="",
        address="",
        shipping_price=200
    )

    total = 0
    for product in wishlist.products.all():
        size = wishlist_sizes.get(str(product.id), None)

        # земи точниот ProductQuantity за таа големина
        pq = ProductQuantity.objects.filter(product=product, size=size).first()
        if pq:
            pq.quantity = max(pq.quantity - 1, 0)
            pq.save()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
            price=product.price,
            size=size
        )
        total += product.price

    order.total_price = total
    order.final_price = total + order.shipping_price
    order.save()

    wishlist.products.clear()
    request.session['wishlist_sizes'] = {}
    request.session.modified = True

    return redirect('order_success', order_id=order.id)


@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order_success.html', {'order': order})
