from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from app.models import Product, ProductQuantity
from .models import Wishlist
from orders.models import Order, OrderItem


# ----------------------------------------
# WISHLIST VIEW
# ----------------------------------------
def wishlist_view(request):
    """Прикажува wishlist, guest или user"""
    wishlist_sizes = request.session.get('wishlist_sizes', {})
    wishlist_quantities = request.session.get('wishlist_quantities', {})

    if request.user.is_authenticated:
        wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
        user_wishlist = True
    else:
        wishlist = None
        user_wishlist = False

    products_with_sizes = []
    total_discount = sum((item.product.price - item.product.new_price) * item.quantity
                         for item in products_with_sizes if item.product.new_price)


    total_price = 0
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
        'total_price': total_price,
        'user_wishlist': user_wishlist,
        'total_discount': total_discount,

    }
    return render(request, 'wishlist/wishlist.html', context)


# ----------------------------------------
# WISHLIST ADD
# ----------------------------------------
def wishlist_add(request, product_id):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        product = get_object_or_404(Product, id=product_id)
        data = json.loads(request.body)
        size = data.get('size', 'Неодредена')
        quantity = int(data.get('quantity', 1))

        key = f"{product.id}_{size}"

        # Session
        wishlist_sizes = request.session.get('wishlist_sizes', {})
        wishlist_sizes[key] = size
        wishlist_quantities = request.session.get('wishlist_quantities', {})

        # Заменува quantity наместо да се сумира
        wishlist_quantities[key] = quantity

        request.session['wishlist_sizes'] = wishlist_sizes
        request.session['wishlist_quantities'] = wishlist_quantities
        request.session.modified = True

        # Ако е најавен, синхронизација со модел
        if request.user.is_authenticated:
            wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
            if not wishlist.products.filter(id=product.id).exists():
                wishlist.products.add(product)

        return JsonResponse({'status': 'success', 'wishlist_count': len(wishlist_sizes)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


# ----------------------------------------
# WISHLIST REMOVE
# ----------------------------------------
def wishlist_remove(request, product_id, size=None):
    wishlist_sizes = request.session.get('wishlist_sizes', {})
    wishlist_quantities = request.session.get('wishlist_quantities', {})

    if size:
        key = f"{product_id}_{size}"
        wishlist_sizes.pop(key, None)
        wishlist_quantities.pop(key, None)
    else:
        keys_to_remove = [k for k in wishlist_sizes if k.startswith(f"{product_id}_")]
        for k in keys_to_remove:
            wishlist_sizes.pop(k, None)
            wishlist_quantities.pop(k, None)

    request.session['wishlist_sizes'] = wishlist_sizes
    request.session['wishlist_quantities'] = wishlist_quantities
    request.session.modified = True

    if request.user.is_authenticated:
        wishlist = get_object_or_404(Wishlist, user=request.user)
        wishlist.products.remove(get_object_or_404(Product, id=product_id))

    return redirect('wishlist')


# ----------------------------------------
# CREATE ORDER
# ----------------------------------------
def create_order(request):
    wishlist_sizes = request.session.get('wishlist_sizes', {})
    wishlist_quantities = request.session.get('wishlist_quantities', {})

    if not wishlist_sizes:
        return redirect('wishlist')

    # User или Guest
    user = request.user if request.user.is_authenticated else None

    # Guest формa
    first_name = request.POST.get('first_name', 'Гостин')
    last_name = request.POST.get('last_name', '')
    email = request.POST.get('email', 'guest@example.com')
    city = request.POST.get('city', '')
    address = request.POST.get('address', '')

    order = Order.objects.create(
        user=user,
        first_name=first_name,
        last_name=last_name,
        email=email,
        city=city,
        address=address,
        shipping_price=200
    )

    total = 0
    for key, size in wishlist_sizes.items():
        prod_id = int(key.split('_')[0])
        product = Product.objects.get(id=prod_id)
        quantity = wishlist_quantities.get(key, 1)

        pq = ProductQuantity.objects.filter(product=product, size=size).first()
        if pq:
            pq.quantity = max(pq.quantity - quantity, 0)
            pq.save()

        OrderItem.objects.create(
            order=order,
            product=product,
            size=size,
            quantity=quantity,
            price=product.price
        )

        total += product.price * quantity

    order.total_price = total
    order.final_price = total + order.shipping_price
    order.save()

    # Испразни session
    request.session['wishlist_sizes'] = {}
    request.session['wishlist_quantities'] = {}
    request.session.modified = True

    return redirect('order_success', order_id=order.id)


# ----------------------------------------
# ORDER SUCCESS
# ----------------------------------------
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order_success.html', {'order': order})
