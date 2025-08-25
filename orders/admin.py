from django.contrib import admin
from .models import Order, OrderItem

# Inline приказ на продукти во нарачка
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Без празни редови
    readonly_fields = ('product', 'quantity', 'price', 'size')
    can_delete = False

# Главен Admin за нарачки
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name',
        'last_name',
        'phone_number',
        'city',
        'cargo',
        'total_price',
        'created_at'
    )
    list_filter = ('cargo', 'city', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone_number', 'user__username', 'city')
    readonly_fields = ('total_price', 'created_at')
    inlines = [OrderItemInline]
    ordering = ('-created_at',)
