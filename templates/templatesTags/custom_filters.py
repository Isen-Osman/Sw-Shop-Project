from django import template

register = template.Library()

@register.filter
def savings(price, new_price):
    try:
        return float(price) - float(new_price)
    except:
        return 0
