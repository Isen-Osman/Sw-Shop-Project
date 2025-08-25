from django.contrib import admin
from .models import Product, ProductQuantity, ProductImage

# Inline за quantity
class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 0
    min_num = 0
    max_num = 6
    can_delete = True
    readonly_fields = ()
    fields = ('size', 'quantity')

# Inline за слики
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    can_delete = True
    readonly_fields = ()
    fields = ('image',)

# Главен Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'color', 'price', 'created_at')
    list_filter = ('category', 'color', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)
    inlines = [ProductQuantityInline, ProductImageInline]
    ordering = ('-created_at',)

    # Ограничи на superuser
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff
