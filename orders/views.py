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

    # HTML содржина за email (за корисникот)
    html_content_user = render_to_string('order/order_confirmation_email.html', {'order': order})
    subject_user = f"Потврда на нарачка #{order.id}"

    # HTML содржина за email (за администратор)
    html_content_admin = render_to_string('order/order_confirmation_email_for_me.html', {'order': order})
    subject_admin = f"Нова нарачка #{order.id}"

    from_email = settings.DEFAULT_FROM_EMAIL

    user_email = [order.user.email]
    email_user = EmailMultiAlternatives(subject_user, '', from_email, user_email)
    email_user.attach_alternative(html_content_user, "text/html")
    email_user.send(fail_silently=False)

    admin_email = [settings.DEFAULT_FROM_EMAIL]  # тука си ја ставаш својата адреса
    email_admin = EmailMultiAlternatives(subject_admin, '', from_email, admin_email)
    email_admin.attach_alternative(html_content_admin, "text/html")
    email_admin.send(fail_silently=False)

    return render(request, 'order/order_confirmation.html', {
        'order': order,
        'wishlist_items_count': wishlist_items_count,
    })
