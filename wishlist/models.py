
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from app.models import Product

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"Wishlist на {self.user.username}"
