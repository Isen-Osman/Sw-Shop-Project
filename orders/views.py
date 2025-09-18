# orders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Order, OrderItem
from .forms import OrderForm
from app.models import ProductQuantity
from concurrent.futures import ThreadPoolExecutor

# ThreadPool за асинхроно праќање email-и
email_executor = ThreadPoolExecutor(max_workers=5)


def send_email_async(subject, html_content, recipient):
    """Функција за асинхроно праќање email."""
    def _send():
        email = EmailMultiAlternatives(
            subject,
            '',
            settings.DEFAULT_FROM_EMAIL,
            [recipient]
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)

    email_executor.submit(_send)


@login_required
def create_order(request):
    wishlist = request.user.wishlist
    wishlist_sizes = request.session.get('wishlist_sizes', {})
    wishlist_quantities = request.session.get('wishlist_quantities', {})

    if not wishlist.products.exists():
        return redirect('wishlist')

    products_with_details = []
    total_price = 0

    for key, size in wishlist_sizes.items():
        prod_id = int(key.split('_')[0])
        product = wishlist.products.get(id=prod_id)
        quantity = int(wishlist_quantities.get(key, 1))
        products_with_details.append({
            'product': product,
            'size': size,
            'quantity': quantity,
        })
        total_price += product.price * quantity

    shipping_price = 0 if total_price >= 2000 else 150
    final_price = total_price + shipping_price

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total_price
            order.final_price = final_price
            order.cargo = shipping_price
            order.save()

            for item in products_with_details:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    size=item['size'],
                    quantity=item['quantity'],
                    price=item['product'].price
                )

            wishlist.products.clear()
            request.session['wishlist_sizes'] = {}
            request.session['wishlist_quantities'] = {}
            request.session.modified = True

            # Redirect за да се избегне повторно POST при refresh
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'order/create_order.html', {
        'form': form,
        'products_with_details': products_with_details,
        'total_price': total_price,
        'shipping_price': shipping_price,
        'final_price': final_price,
        'wishlist_items_count': len(products_with_details),
    })


@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    wishlist_items_count = request.user.wishlist.products.count()

    if order.cargo is None:
        order.cargo = 0  # Бесплатна достава ако не е зададена

    # Испрати email само ако не е испратен
    if not order.email_sent:
        # Email за корисник
        html_user = render_to_string('order/order_confirmation_email.html', {'order': order})
        send_email_async(
            f"Потврда на нарачка #{order.id}",
            html_user,
            order.user.email
        )

        # Email за администратор
        html_admin = render_to_string('order/order_confirmation_email_for_me.html', {'order': order})
        send_email_async(
            f"Нова нарачка #{order.id}",
            html_admin,
            'shopsw108@gmail.com'
        )

        # Обележи дека email е испратен
        order.email_sent = True
        order.save()

    # Намалување на quantity за секој купен производ
    for item in order.items.all():
        pq = ProductQuantity.objects.filter(product=item.product, size=item.size).first()
        if pq:
            pq.quantity = max(pq.quantity - item.quantity, 0)
            pq.save()

    return render(request, 'order/order_confirmation.html', {
        'order': order,
        'wishlist_items_count': wishlist_items_count,
    })


def delivery(request):
    """Страница за испорака и враќање на производи."""
    return render(request, 'delivery/delivery.html')