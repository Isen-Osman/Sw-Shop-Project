from django import forms
from .models import Product, ProductQuantity, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'color', 'category', 'subcategory',]

class ProductQuantityForm(forms.ModelForm):
    class Meta:
        model = ProductQuantity
        fields = ['size', 'quantity']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
