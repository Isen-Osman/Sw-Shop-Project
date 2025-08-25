from django import forms
from .models import Order
import re

MACEDONIAN_CITIES = [
    ("Аеродром", "Аеродром"),
    ("Берово", "Берово"),
    ("Битола", "Битола"),
    ("Богданци", "Богданци"),
    ("Валандово", "Валандово"),
    ("Велес", "Велес"),
    ("Виница", "Виница"),
    ("Гевгелија", "Гевгелија"),
    ("Гостивар", "Гостивар"),
    ("Дебар", "Дебар"),
    ("Делчево", "Делчево"),
    ("Кавадарци", "Кавадарци"),
    ("Кичево", "Кичево"),
    ("Кочани", "Кочани"),
    ("Кратово", "Кратово"),
    ("Крива Паланка", "Крива Паланка"),
    ("Крушево", "Крушево"),
    ("Куманово", "Куманово"),
    ("Македонска Каменица", "Македонска Каменица"),
    ("Македонски Брод", "Македонски Брод"),
    ("Неготино", "Неготино"),
    ("Охрид", "Охрид"),
    ("Пехчево", "Пехчево"),
    ("Прилеп", "Прилеп"),
    ("Пробиштип", "Пробиштип"),
    ("Радовиш", "Радовиш"),
    ("Ресен", "Ресен"),
    ("Свети Николе", "Свети Николе"),
    ("Скопје", "Скопје"),
    ("Струмица", "Струмица"),
    ("Струга", "Струга"),
    ("Тетово", "Тетово"),
    ("Штип", "Штип"),
]


class OrderForm(forms.ModelForm):
    city = forms.ChoiceField(
        choices=[("", "Избери град")] + MACEDONIAN_CITIES,
        widget=forms.Select(attrs={'class': 'input-class'}),
        label='Град'
    )

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'city', 'phone_number', 'address', 'comment']

        labels = {
            'first_name': 'Име',
            'last_name': 'Презиме',
            'phone_number': 'Телефонски број',
            'address': 'Адреса',
            'comment': 'Коментар'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Име'}),
            'last_name': forms.TextInput(attrs={'class': 'input-class', 'placeholder': 'Презиме'}),
            'phone_number': forms.TextInput(attrs={
                'class': 'input-class',
                'placeholder': '070 123 456',
            }),
            'address': forms.Textarea(attrs={'class': 'input-class', 'rows': 3, 'placeholder': 'Адреса'}),
            'comment': forms.Textarea(attrs={'class': 'input-class', 'rows': 2, 'placeholder': 'Коментар (опционално)'}),
        }

        error_messages = {
            'first_name': {'required': 'Ова поле е задолжително'},
            'last_name': {'required': 'Ова поле е задолжително'},
            'city': {'required': 'Ова поле е задолжително'},
            'phone_number': {'required': 'Ова поле е задолжително'},
            'address': {'required': 'Ова поле е задолжително'},
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and len(first_name.strip()) < 3:
            raise forms.ValidationError("Името мора да има најмалку 3 букви")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and len(last_name.strip()) < 3:
            raise forms.ValidationError("Презимето мора да има најмалку 3 букви")
        return last_name

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone:
            # Отстрани празни места и цртички
            phone = re.sub(r'[\s\-]', '', phone)

            # Проверка дали бројот е валиден за Македонија
            if not re.match(r'^07\d{7}$', phone):
                raise forms.ValidationError(
                    "Телефонскиот број мора да биде во формат: 070123456"
                )
        return phone
