from django.contrib import admin
from .models import Product, ProductImage, ProductQuantity


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'category', 'created_at')
    inlines = [ProductQuantityInline, ProductImageInline]


    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductQuantity)
admin.site.register(ProductImage)