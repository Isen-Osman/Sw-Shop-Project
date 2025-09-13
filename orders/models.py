from django.db import models
from django.contrib.auth.models import User
from app.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50, choices=(("Standard", "Standard"), ("Express", "Express")))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    comment = models.TextField(max_length=100, blank=True)
    email_sent = models.BooleanField(default=False)


    def __str__(self):
        return f"Order #{self.id} од {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10, blank=True, null=True)


    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
