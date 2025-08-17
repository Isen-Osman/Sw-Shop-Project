
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from app.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    for product in wishlist.products.all():
        product.new_price = product.price + 200

    total_price = sum([product.price for product in wishlist.products.all()])
    return render(request, 'wishlist.html', {'wishlist': wishlist, 'total_price': total_price})


@login_required
def wishlist_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect('wishlist')

@login_required
def wishlist_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.products.remove(product)
    return redirect('wishlist')

