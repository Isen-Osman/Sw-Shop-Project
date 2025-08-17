from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product, ProductImage, Category


def product_list(request):
    products = Product.objects.all()

    # Додај нов атрибут за новата цена
    for product in products:
        product.new_price = product.price + 200  # новата променлива

    return render(request, 'product_page.html', {'products': products})


def recently_added_products(request):
    products = Product.objects.all().order_by('-created_at')[:5]  # последни 5 продукти

    # Додај нов атрибут за новата цена
    for product in products:
        product.new_price = product.price + 200  # новата променлива

    return render(request, 'home_page.html', {'products': products})


def product_add(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)

        # take uploaded images
        images = request.FILES.getlist('images')

        if product_form.is_valid():
            product = product_form.save()

            # save images separately
            for img in images:
                ProductImage.objects.create(product=product, image=img)

            return redirect('products')
    else:
        product_form = ProductForm()

    return render(request, 'product_add.html', {'form': product_form})



def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        images = request.FILES.getlist('images')

        if form.is_valid():
            form.save()

            # Додај нови слики ако има
            for img in images:
                ProductImage.objects.create(product=product, image=img)

            return redirect('products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_edit.html', {'form': form, 'product': product})


def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('products')


def product_detail(request, product_id):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=product_id)

    # Додај нов атрибут за новата цена
    for product in products:
        product.new_price = product.price + 200  # новата променлива

    return render(request, 'product_detail.html', {'product': product})

def products_by_category(request, category_name):
    products = Product.objects.filter(category=category_name)
    return render(request, 'home.html', {'products': products, 'category_name': category_name})