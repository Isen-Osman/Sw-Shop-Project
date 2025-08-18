from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'city', 'address', 'cargo']

    # Означуваме сите полиња како не-обврзувачки


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name in self.fields:
        self.fields[field_name].required = False  # полето не е обврзувачко, корисникот може да го пополни
        self.fields[field_name].widget.attrs.update({'placeholder': field_name.replace('_', ' ').capitalize()})
