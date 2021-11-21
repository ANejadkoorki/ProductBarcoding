from django.db import models
from django.core.validators import RegexValidator
from .categories_models import *
from .other_models import *

five_digit_validator = RegexValidator(
    regex="/^[0-9]{4}[1-9]{1}$/gm",
    message="the code should be matched with the correct format : 00001-99999",
)


# Create your models here.

class Product(models.Model):
    code = models.CharField(
        verbose_name="product code",
        validators=[five_digit_validator],
        unique=True,
        max_length=5,
    )

    third_category = models.ForeignKey(
        to=ThirdCategory,
        on_delete=models.CASCADE,
    )

    colour = models.ForeignKey(
        to=Colour,
        on_delete=models.PROTECT,
    )

    size = models.ForeignKey(
        to=Size,
        on_delete=models.PROTECT,
    )

    store = models.ForeignKey(
        to=Store,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        verbose_name="product name",
        max_length=200,
    )

    class Meta:
        unique_together = ['name', 'code']


