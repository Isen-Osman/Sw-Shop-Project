from django.shortcuts import render, redirect, get_object_or_404

from orders.models import OrderItem, Order
from .models import Wishlist
from app.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    for product in wishlist.products.all():
        product.new_price = product.price + 200

    total_price = sum([product.price for product in wishlist.products.all()])
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist, 'total_price': total_price})


@login_required
def wishlist_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    size = request.GET.get('size')  # Примаме ?size=S од product_detail

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    # Ако сакаш само ManyToManyField без through модел
    wishlist.products.add(product)

    # Чување на избраната големина во session или во поврзан модел (препорачливо through модел)
    # Пример со session:
    if size:
        if 'wishlist_sizes' not in request.session:
            request.session['wishlist_sizes'] = {}
        request.session['wishlist_sizes'][str(product.id)] = size
        request.session.modified = True

    return redirect('wishlist')


@login_required
def wishlist_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.products.remove(product)
    return redirect('wishlist')


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