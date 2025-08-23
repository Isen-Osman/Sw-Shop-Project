from .models import Category

def categories_processor(request):
    # Ги враќаме сите категории од enum како tuple (value, label)
    return {
        "all_categories": Category.choices
    }
