from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .forms import ProductForm
from .models import Product, ProductQuantity, ProductImage, Size
from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages


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

    return render(request, 'products/product_page.html', {'products': products})


def recently_added_products(request):
    products = Product.objects.all().order_by('-created_at')[:5]

    for product in products:
        product.new_price = product.price + 200

    return render(request, 'home/home_page.html', {'products': products})


def product_add(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        images = request.FILES.getlist('images')

        if product_form.is_valid():
            product = product_form.save()

            for size in Size.values:
                qty = int(request.POST.get(f'quantity_{size}', 0))
                if qty > 0:
                    ProductQuantity.objects.create(product=product, size=size, quantity=qty)

            for img in images:
                ProductImage.objects.create(product=product, image=img)

            return redirect('products')
    else:
        product_form = ProductForm()

    return render(request, 'products/product_add.html', {
        'form': product_form,
        'sizes': Size.values,
    })


def product_edit(request, product_id):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('home')

    product = get_object_or_404(Product, id=product_id)
    sizes = Size.values

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        images = request.FILES.getlist('images')

        if form.is_valid():
            form.save()

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

            for img in images:
                ProductImage.objects.create(product=product, image=img)

            return redirect('products')
    else:
        form = ProductForm(instance=product)

    size_quantities = {}
    for size in sizes:
        pq = ProductQuantity.objects.filter(product=product, size=size).first()
        size_quantities[size] = pq.quantity if pq else 0

    size_data = [(size, size_quantities[size]) for size in sizes]

    return render(request, 'products/product_edit.html', {
        'form': form,
        'product': product,
        'sizes': sizes,
        'size_quantities': size_quantities,
        'size_data': size_data,
    })


def product_delete(request, pk):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('home')

    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    available_sizes = product.quantities.filter(quantity__gt=0)
    product.new_price = product.price + 200
    context = {
        'product': product,
        'available_sizes': available_sizes,
    }
    return render(request, 'products/product_detail.html', context)


def products_by_category(request, category_name):
    products = Product.objects.filter(category=category_name)

    for product in products:
        product.new_price = product.price + 200

    return render(request, 'products/product_page.html', {
        'products': products,
        'category_name': category_name.capitalize()
    })


def collections_page(request):
    return render(request, 'lg/collections_page.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'registration/login.html')


def profile_view(request):
    return render(request, 'registration/profile.html')


def custom_logout(request):
    logout(request)
    return redirect('/')


def search_view(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()

        for p in products:
            results.append({
                'id': p.id,
                'name': p.name,
                'price': p.price,
                'image': p.images.first().image.url if p.images.exists() else '',
            })

    return JsonResponse({'results': results})


def about_us(request):
    return render(request, "aboutUs/aboutUs.html")


def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Име: {first_name}\nПрезиме: {last_name}\nЕ-маил: {email}\n\nПорака:\n{message}"

        send_mail(
            subject=f'Нова порака од {first_name} {last_name}',
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,  # На пример 'web@swshop.com'
            recipient_list=['shopsw108@gmail.com'],  # Твојот e-mail
            fail_silently=False,
        )
        messages.success(request, 'Вашата порака е испратена успешно!')
        return redirect('contact')
    return render(request, 'contact/contact.html')
