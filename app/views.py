from django.shortcuts import render

from app.models import Product


def product_list(request):
    products = Product.objects.all()

    return render(request, 'product_page.html', {'products': products})


# def home_page(request):
#     products = Product.objects.all().order_by('-created_at')[:5]
#
#     return render(request, 'home_page.html', {'products': products})