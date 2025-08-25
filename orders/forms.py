from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'city', 'phone_number', 'address', 'comment']

        labels = {
            'first_name': 'Име',
            'last_name': 'Презиме',
            'city': 'Град',
            'phone_number': 'Број',
            'address': 'Адреса',
            'comment': 'Коментар'

        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-class'}),
            'last_name': forms.TextInput(attrs={'class': 'input-class'}),
            'city': forms.TextInput(attrs={'class': 'input-class'}),
            'phone_number': forms.TextInput(attrs={'class': 'input-class'}),
            'address': forms.Textarea(attrs={'class': 'input-class', 'rows': 3}),
            'cargo': forms.NumberInput(attrs={'class': 'input-class'}),
        }
        error_messages = {
            'first_name': {'required': 'Ова поле е задолжително'},
            'last_name': {'required': 'Ова поле е задолжително'},
            'city': {'required': 'Ова поле е задолжително'},
            'phone_number': {'required': 'Ова поле е задолжително'},
            'address': {'required': 'Ова поле е задолжително'},
            'cargo': {'required': 'Ова поле е задолжително'},
        }


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name in self.fields:
        self.fields[field_name].required = False  # полето не е обврзувачко, корисникот може да го пополни
        self.fields[field_name].widget.attrs.update({'placeholder': field_name.replace('_', ' ').capitalize()})
