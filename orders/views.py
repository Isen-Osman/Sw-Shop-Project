from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from app.models import ProductQuantity
from .models import OrderItem, Order
from .forms import OrderForm


@login_required
def create_order(request):
    wishlist = request.user.wishlist  # ја земаме Wishlist за тековниот корисник
    products = wishlist.products.all()

    total_price = sum(p.price for p in products)
    shipping_price = 200
    final_price = total_price + shipping_price

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total_price
            order.save()

            # ги додаваме продуктите како OrderItem
            for product in products:
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=1,  # quantity може да се додаде ако сакате
                    price=product.price
                )

            # по креирање на order, ја празниме Wishlist
            wishlist.products.clear()

            return redirect('order_success', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'order/create_order.html', {
        'form': form,
        'products': products,
        'total_price': total_price,
        'shipping_price': shipping_price,
        'final_price': final_price
    })


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Намалување на quantity на продуктите (без size)
    for item in order.items.all():
        try:
            pq = ProductQuantity.objects.filter(product=item.product).first()  # првиот ProductQuantity
            if pq:
                pq.quantity -= item.quantity
                pq.save()
        except ProductQuantity.DoesNotExist:
            pass

    return render(request, 'order/order_success.html', {'order': order})