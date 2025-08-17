from django.contrib import admin
from .models import Product, ProductImage, ProductQuantity


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

    # Достапно само за superuser
    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 5

    list_filter = ('category', 'color')
    search_fields = ('name', 'description')

    # Достапно само за superuser
    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'category', 'created_at')
    inlines = [ProductQuantityInline, ProductImageInline]

    # Достапно само за superuser
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    # Ако сакаш superuser да види сите полиња, а други само read-only
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return [field.name for field in self.model._meta.fields]
        return []
