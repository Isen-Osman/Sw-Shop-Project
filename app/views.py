from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product, ProductImage, Category


def product_list(request):
    products = Product.objects.all()

    # Филтрирање по категорија
    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)

    # Филтрирање по ценовен опсег
    price_range = request.GET.get('price_range')
    if price_range:
        if price_range == '0-500':
            products = products.filter(price__lte=500)
        elif price_range == '500-1000':
            products = products.filter(price__gte=500, price__lte=1000)
        elif price_range == '1000+':
            products = products.filter(price__gte=1000)

    # Подредување
    sort = request.GET.get('sort')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')
    elif sort == 'oldest':
        products = products.order_by('created_at')

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


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Додај нов атрибут за новата цена
    product.new_price = product.price + 200

    return render(request, 'product_detail.html', {'product': product})


def products_by_category(request, category_name):
    # филтрирај продукти според параметарот од URL
    products = Product.objects.filter(category=category_name)

    # додај нов атрибут за new_price
    for product in products:
        product.new_price = product.price + 200

    return render(request, 'product_page.html', {
        'products': products,
        'category_name': category_name.capitalize()
    })


def collections_page(request):
    return render(request, 'collections_page.html', )
