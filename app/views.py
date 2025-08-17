from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product, ProductImage


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_page.html', {'products': products})


def recently_added_products(request):
    products = Product.objects.all().order_by('-created_at')[:5]  # последни 5 продукти

    return render(request, 'home_page.html', {'products': products})


def product_add(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        images = request.FILES.getlist('images')  # земи сите прикачени фајлови

        if product_form.is_valid():
            product = product_form.save()

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
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
