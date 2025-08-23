from .models import Category

def categories_processor(request):
    # Ги враќаме сите категории од enum како tuple (value, label)
    return {
        "all_categories": Category.choices
    }

def wishlist_counter(request):
    count = 0
    if request.user.is_authenticated:
        try:
            count = request.user.wishlist.products.count()
        except AttributeError:
            count = 0
    return {
        'wishlist_items_count': count
    }