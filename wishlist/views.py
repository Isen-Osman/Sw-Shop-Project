from django.shortcuts import render, redirect, get_object_or_404

from orders.models import OrderItem, Order
from .models import Wishlist
from app.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def wishlist_view(request):
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        wishlist = None

        # Get sizes from session
    wishlist_sizes = request.session.get('wishlist_sizes', {})

    # Create a list of products with their sizes
    products_with_sizes = []
    total_price = 0

    if wishlist:
        for product in wishlist.products.all():
            product_size = wishlist_sizes.get(str(product.id), 'Неодредена')
            products_with_sizes.append({
                'product': product,
                'size': product_size
            })
            total_price += product.price

    context = {
        'wishlist': wishlist,
        'total_price': total_price,
        'products_with_sizes': products_with_sizes,
    }
    return render(request, 'wishlist/wishlist.html', context)

from django.http import JsonResponse
import json


@login_required(login_url='/accounts/google/login/')
def wishlist_add(request, product_id):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            product = get_object_or_404(Product, id=product_id)
            data = json.loads(request.body)
            size = data.get('size')

            wishlist, created = Wishlist.objects.get_or_create(user=request.user)

            # Проверете дали производот веќе е во кошничката
            if not wishlist.products.filter(id=product.id).exists():
                wishlist.products.add(product)

            # Зачувајте ја големината во сесија
            if size:
                wishlist_sizes = request.session.get('wishlist_sizes', {})
                wishlist_sizes[str(product.id)] = size
                request.session['wishlist_sizes'] = wishlist_sizes
                request.session.modified = True

            return JsonResponse({
                'status': 'success',
                'message': 'Продуктот е додаден во кошничка!',
                'wishlist_count': wishlist.products.count()
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


@login_required(login_url='/accounts/google/login/')
def wishlist_add(request, product_id):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Handle AJAX request
        product = get_object_or_404(Product, id=product_id)

        try:
            data = json.loads(request.body)
            size = data.get('size')

            wishlist, created = Wishlist.objects.get_or_create(user=request.user)
            wishlist.products.add(product)

            if size:
                wishlist_sizes = request.session.get('wishlist_sizes', {})
                wishlist_sizes[str(product.id)] = size
                request.session['wishlist_sizes'] = wishlist_sizes
                request.session.modified = True

            return JsonResponse({'status': 'success', 'message': 'Продуктот е додаден во кошничка!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    # Handle non-AJAX requests if needed
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


@login_required
def create_order(request):
    wishlist = get_object_or_404(Wishlist, user=request.user)

    if not wishlist.products.exists():
        return redirect("wishlist")

    # креираме празна нарачка
    order = Order.objects.create(
        user=request.user,
        first_name=request.user.first_name or "Име",
        last_name=request.user.last_name or "Презиме",
        email=request.user.email or "test@example.com",
        city="",
        address="",
        shipping_price=200  # фиксно карго за тест
    )

    total = 0
    for product in wishlist.products.all():
        OrderItem.objects.create(
            order=order,
            product=product,
            price=product.price,
            quantity=1
        )
        total += product.price

    order.total_price = total
    order.final_price = total + order.shipping_price
    order.save()

    # испразни wishlist
    wishlist.products.clear()

    return redirect("order_detail", pk=order.pk)


@login_required
def wishlist_remove(request, product_id):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    product = get_object_or_404(Product, id=product_id)

    if wishlist.products.filter(id=product.id).exists():
        wishlist.products.remove(product)

        # избриши и од session за големина
        wishlist_sizes = request.session.get('wishlist_sizes', {})
        if str(product.id) in wishlist_sizes:
            del wishlist_sizes[str(product.id)]
            request.session['wishlist_sizes'] = wishlist_sizes
            request.session.modified = True

    return redirect('wishlist')