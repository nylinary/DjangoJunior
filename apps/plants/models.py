from django.db import models
from django.core.validators import MinValueValidator

class Plant(models.Model):
    class Colors(models.TextChoices):
        GREEN = "green", "Зелёный"
        RED = "red", "Красный"
        BLUE = "blue", "Синий" 

    name = models.CharField(max_length=100)
    color = models.CharField(choices=Colors, max_length=15)
    price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0)])
    # type = ...