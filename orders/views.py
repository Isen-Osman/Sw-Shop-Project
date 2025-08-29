# orders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from app.models import ProductQuantity
from .models import OrderItem, Order
from .forms import OrderForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@login_required
def create_order(request):
    wishlist = request.user.wishlist

    wishlist_sizes = request.session.get('wishlist_sizes', {})
    wishlist_quantities = request.session.get('wishlist_quantities', {})

    if not wishlist.products.exists():
        return redirect('wishlist')

    # Изгради list за template
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

    shipping_price = 150
    final_price = total_price + shipping_price

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total_price
            order.final_price = final_price
            order.save()

            # Креирај OrderItem со точен size и quantity
            for item in products_with_details:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    size=item['size'],
                    quantity=item['quantity'],
                    price=item['product'].price
                )

            # Испразни wishlist и session
            wishlist.products.clear()
            request.session['wishlist_sizes'] = {}
            request.session['wishlist_quantities'] = {}
            request.session.modified = True

            return redirect('order_success', order_id=order.id)
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
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Намалување на quantity за секој купен производ и големина
    for item in order.items.all():
        pq = ProductQuantity.objects.filter(product=item.product, size=item.size).first()
        if pq:
            pq.quantity -= item.quantity
            if pq.quantity < 0:
                pq.quantity = 0
            pq.save()

    return redirect('order_confirmation', order_id=order.id)


@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    wishlist_items_count = request.user.wishlist.products.count()

    # HTML содржина за email
    html_content = render_to_string('order/order_confirmation_email.html', {'order': order})
    subject = f"Потврда на нарачка #{order.id}"
    from_email = settings.DEFAULT_FROM_EMAIL

    # Испраќање до корисникот
    user_email = [order.user.email]

    # Испраќање до тебе (администратор)
    admin_email = ['shopsw108@gmail.com']  # стави го твојот email овде

    # Создај email објект
    email = EmailMultiAlternatives(subject, '', from_email, user_email)
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)

    # Копија за тебе
    admin_email_msg = EmailMultiAlternatives(subject, '', from_email, admin_email)
    admin_email_msg.attach_alternative(html_content, "text/html")
    admin_email_msg.send(fail_silently=False)

    return render(request, 'order/order_confirmation.html', {
        'order': order,
        'wishlist_items_count': wishlist_items_count,
    })
