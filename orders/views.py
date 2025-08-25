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
    products = wishlist.products.all()

    if not products.exists():
        return redirect('wishlist')

    total_price = sum(product.price for product in products)
    shipping_price = 150
    final_price = total_price + shipping_price

    # Земаме size од session
    wishlist_sizes = request.session.get('wishlist_sizes', {})
    product_size = request.session.get('product_size', {})

    # Додавање на products_with_sizes за template
    products_with_sizes = []
    for product in products:
        size = wishlist_sizes.get(str(product.id), 'Неодредена')
        products_with_sizes.append({
            'product': product,
            'size': size
        })

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total_price
            order.final_price = final_price
            order.save()

            # додавање на продукти во нарачка со точен size
            for product in products:
                product_size = wishlist_sizes.get(str(product.id), 'Неодредена')
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=1,
                    price=product.price,
                    size=product_size
                )

            # испразни wishlist и session за size
            wishlist.products.clear()
            if 'wishlist_sizes' in request.session:
                del request.session['wishlist_sizes']

            return redirect('order_success', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'order/create_order.html', {
        'form': form,
        'products': products,
        'products_with_sizes': products_with_sizes,  # <-- додадено за size
        'total_price': total_price,
        'shipping_price': shipping_price,
        'final_price': final_price,
        'wishlist_items_count': products.count(),
        'wishlist_sizes': wishlist_sizes,
        'product_size': product_size,
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
    # Нова верзија (точно за твојот модел)
    wishlist_items_count = request.user.wishlist.products.count()

    # Испраќање email потврда
    html_content = render_to_string('order/order_confirmation_email.html', {'order': order})
    subject = f"Потврда на нарачка #{order.id}"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [order.user.email]

    email = EmailMultiAlternatives(subject, '', from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)

    return render(request, 'order/order_confirmation.html', {
        'order': order,
        'wishlist_items_count': wishlist_items_count,
    })
