from django.db import models

# Enum-ови за големини и боја
class Size(models.TextChoices):
    XS = "XS", "XS"
    S = "S", "S"
    M = "M", "M"
    L = "L", "L"
    XL = "XL", "XL"

class Color(models.TextChoices):
    RED = "RED", "Red"
    BLUE = "BLUE", "Blue"
    GREEN = "GREEN", "Green"
    BLACK = "BLACK", "Black"
    WHITE = "WHITE", "White"

class Category(models.TextChoices):
    BRAS = "bras", "Bras"
    PANTIES = "panties", "Panties"
    LINGERIE = "lingerie", "Lingerie"
    PAJAMAS = "pajamas", "Pajamas"

# Главен модел Product
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20, choices=Color.choices)
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.BRAS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

# Quantity по големина
class ProductQuantity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='quantities')
    size = models.CharField(max_length=5, choices=Size.choices)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.size}: {self.quantity}"

# Повеќе слики за продукт
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name}"


