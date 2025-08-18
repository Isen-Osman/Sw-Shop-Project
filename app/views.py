from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product, ProductImage, ProductQuantity
from django.forms.models import inlineformset_factory


def product_list(request):
    products = Product.objects.all()

    # Додај нов атрибут за новата цена
    for product in products:
        product.new_price = product.price + 200  # новата променлива

    return render(request, 'products/product_page.html', {'products': products})


def recently_added_products(request):
    products = Product.objects.all().order_by('-created_at')[:5]  # последни 5 продукти

    # Додај нов атрибут за новата цена
    for product in products:
        product.new_price = product.price + 200  # новата променлива

    return render(request, 'home/home_page.html', {'products': products})


from .models import Product, ProductQuantity, ProductImage, Size


def product_add(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        images = request.FILES.getlist('images')

        if product_form.is_valid():
            product = product_form.save()

            # зачувај quantity за секоја size
            for size in Size.values:
                qty = int(request.POST.get(f'quantity_{size}', 0))
                if qty > 0:
                    ProductQuantity.objects.create(product=product, size=size, quantity=qty)

            # зачувај слики
            for img in images:
                ProductImage.objects.create(product=product, image=img)

            return redirect('products')
    else:
        product_form = ProductForm()

    return render(request, 'products/product_add.html', {
        'form': product_form,
        'sizes': Size.values,  # праќаме ги сите size во template
    })


def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    sizes = Size.values  # листа на сите големини (M, L, XL...)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        images = request.FILES.getlist('images')

        if form.is_valid():
            form.save()

            # Зачувај quantity за секоја size
            for size in sizes:
                qty_str = request.POST.get(f'quantity_{size}', '0')
                try:
                    qty = int(qty_str)
                except ValueError:
                    qty = 0

                if qty >= 0:
                    ProductQuantity.objects.update_or_create(
                        product=product,
                        size=size,
                        defaults={'quantity': qty}
                    )

            # Додај нови слики ако има
            for img in images:
                ProductImage.objects.create(product=product, image=img)

            return redirect('products')
    else:
        form = ProductForm(instance=product)

    # Подготовка на quantity за секој size за template
    size_quantities = {}
    for size in sizes:
        pq = ProductQuantity.objects.filter(product=product, size=size).first()
        size_quantities[size] = pq.quantity if pq else 0

    # Подготовка на size_data (size, quantity) tuple list
    size_data = [(size, size_quantities[size]) for size in sizes]

    return render(request, 'products/product_edit.html', {
        'form': form,
        'product': product,
        'sizes': sizes,
        'size_quantities': size_quantities,
        'size_data': size_data,  # додаено за template
    })


def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('products')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    available_sizes = product.quantities.filter(quantity__gt=0)
    context = {
        'product': product,
        'available_sizes': available_sizes,
    }
    return render(request, 'products/product_detail.html', context)


def products_by_category(request, category_name):
    products = Product.objects.filter(category=category_name)
    return render(request, 'home.html', {'products': products, 'category_name': category_name})
