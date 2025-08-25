
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from app.models import Product
from app.models import Size

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"Wishlist на {self.user.username}"


class WishlistProduct(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=5, choices=Size.choices, default=Size.M)

    def __str__(self):
        return f"{self.product.name} ({self.size})"