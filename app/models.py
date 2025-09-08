from django.db import models


# Enum-ови за големини и боја
class Size(models.TextChoices):
    # Стандардни големини
    XS = "XS", "XS"
    S = "S", "S"
    M = "M", "M"
    L = "L", "L"
    XL = "XL", "XL"
    XXL = "XXL", "XXL"
    XXXL = "XXXL", "XXXL"

    # Големини за градници
    SIZE_70 = "70", "70"
    SIZE_75 = "75", "75"
    SIZE_80 = "80", "80"
    SIZE_85 = "85", "85"
    SIZE_90 = "90", "90"
    SIZE_95 = "95", "95"
    SIZE_100 = "100", "100"
    SIZE_105 = "105", "105"
    SIZE_110 = "110", "110"
    SIZE_115 = "115", "115"
    SIZE_120 = "120", "120"
    SIZE_125 = "125", "125"
    SIZE_130 = "130", "130",
    STANDARD = "Standard", "Standard"


class Color(models.TextChoices):
    RED = "RED", "Црвена"
    BLUE = "BLUE", "Плава"
    GREEN = "GREEN", "Зелена"
    BLACK = "BLACK", "Црна"
    WHITE = "WHITE", "Бела"
    YELLOW = "YELLOW", "Жолта"
    ORANGE = "ORANGE", "Портокалова"
    PURPLE = "PURPLE", "Виолетова"
    PINK = "PINK", "Розева"
    BROWN = "BROWN", "Кафена"
    GRAY = "GRAY", "Сива"
    SILVER = "SILVER", "Сребрена"
    GOLD = "GOLD", "Златна"
    BEIGE = "BEIGE", "Беж"
    CYAN = "CYAN", "Цијан"
    MAGENTA = "MAGENTA", "Магента"
    NAVY = "NAVY", "Морнарско сина"
    TEAL = "TEAL", "Тиркизна"
    OLIVE = "OLIVE", "Маслинеста"
    MAROON = "MAROON", "Бордо"


class Category(models.TextChoices):
    # Главни категории
    BRAS = "BRAS", "Градници"
    PANTIES = "PANTIES", "Килоти"
    LINGERIE = "LINGERIE", "Приватна"
    PAJAMAS = "PAJAMAS", "Пижами",
    TSHIRT = "TSHIRT", "Маици",
    BODICES = "BODICES", 'Мидери',
    LEGGINGS = 'LEGGINGS', 'Хеланки',
    NIGHTCLOTHES = 'NIGHTCLOTHES', 'Ноќници',
    KITS = 'KITS', 'Комплети',
    BABY_DOLL = 'BABY_DOLL', 'Бебидол',
    ACCESSORIES = 'ACCESSORIES', 'Додатоци',

    # Подкатегории за килоти
    PANTIES_TANGA = "PANTIES_TANGA", "Килоти - Танга",
    PANTIES_HALF_TANGA = "PANTIES_HALF_TANGA", "Килоти - Полутанга",
    PANTIES_HIGH_WAIST = "PANTIES_HIGH_WAIST", "Килоти - Високи",
    BOXER_PANTIES = 'BOXER_PANTIES', 'Килоти - Боксерки',

    # Подкатегории за градници
    BRAS_PUSH_UP = "BRAS_PUSH_UP", "Градници - Push-up",
    BRAS_SPORT = "BRAS_SPORT", "Градници - Спортски",
    BRAS_LACE = "BRAS_LACE", "Градници - Чипкани",
    BRAS_UNDERWIRE = 'BRAS_UNDERWIRE', 'Градници - Без жица',

    # Подкатегории за пижами
    PAJAMAS_SHORT = "PAJAMAS_SHORT", "Пижами - Кратки",
    PAJAMAS_LONG = "PAJAMAS_LONG", "Пижами - Долги",


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
    size = models.CharField(max_length=255, choices=Size.choices)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.size}: {self.quantity}"


# Повеќе слики за продукт
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name}"
