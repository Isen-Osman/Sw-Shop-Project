from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings

from app.models import ProductQuantity
from .models import OrderItem, Order
from .forms import OrderForm


@login_required
def create_order(request):
    wishlist = request.user.wishlist
    products = wishlist.products.all()

    # Број на продукти во wishlist
    wishlist_items_count = products.count()

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

            for product in products:
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=1,
                    price=product.price
                )

            wishlist.products.clear()  # празни wishlist по нарачката
            return redirect('order_success', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'order/create_order.html', {
        'form': form,
        'products': products,
        'total_price': total_price,
        'shipping_price': shipping_price,
        'final_price': final_price,
        'wishlist_items_count': wishlist_items_count,  # <--- додај го тука
    })


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Намалување на quantity на продуктите, без да се оди под 0
    for item in order.items.all():
        pq_list = ProductQuantity.objects.filter(product=item.product)
        for pq in pq_list:
            pq.quantity -= item.quantity
            if pq.quantity < 0:
                pq.quantity = 0  # никогаш не оди под 0
            pq.save()

    # Префрлање кон order_confirmation за прикажување и праќање на е-мејл
    return redirect('order_confirmation', order_id=order.id)


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Број на продукти во wishlist (на пример, за navbar)
    wishlist_items_count = request.user.wishlist.products.count()

    # HTML шаблон со детали за нарачката
    html_content = render_to_string('order/order_confirmation_email.html', {'order': order})

    subject = f"Потврда на нарачка #{order.id}"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [order.user.email]

    email = EmailMultiAlternatives(subject, '', from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)

    return render(request, 'order/order_confirmation.html', {
        'order': order,
        'wishlist_items_count': wishlist_items_count,  # <--- додај го тука
    })
