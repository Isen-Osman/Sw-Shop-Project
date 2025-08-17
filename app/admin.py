from django.contrib import admin
from .models import Product, ProductImage, ProductQuantity

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 5

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'category', 'created_at')
    inlines = [ProductQuantityInline, ProductImageInline]
