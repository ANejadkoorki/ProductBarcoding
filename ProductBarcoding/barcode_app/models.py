from django.db import models
from django.core.validators import RegexValidator
from smart_selects.db_fields import ChainedForeignKey

from .categories_models import MotherCategory, SecondCategory, ThirdCategory
from .other_models import Store, Size, Colour

five_digit_validator = RegexValidator(
    regex="^[0-9]{4}[1-9]{1}$",
    message="the code should be matched with the correct format : 00001-99999",
)


# Create your models here.

class Product(models.Model):
    """
        Product objects are made with this model.
    """
    barcode = models.CharField(
        verbose_name="product barcode",
        unique=True,
        max_length=26,
        null=True,
    )
    code = models.CharField(
        verbose_name="product code",
        validators=[five_digit_validator],
        unique=True,
        max_length=5,
    )

    mother_category = models.ForeignKey(
        to=MotherCategory,
        on_delete=models.CASCADE,
        null=True,
    )

    second_category = ChainedForeignKey(
        to=SecondCategory,
        chained_field="mother_category",
        chained_model_field="mother_category",
        sort=True,
        null=True,
    )

    third_category = ChainedForeignKey(
        to=ThirdCategory,
        chained_field="second_category",
        chained_model_field="second_category",
        sort=True,
        null=True,
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

    def set_barcode(self):
        """
            this method set the product barcode
        """
        try:
            self.barcode = f"{self.mother_category.code}-{self.second_category.code}-{self.third_category.code}-" \
                           f"{self.code}-{self.colour.code}-{self.size.code}-{self.store.code}"
            self.save()
            return True
        except:
            return False

    def get_barcode(self):
        """
            this method return the product barcode
        """
        return self.barcode

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ['name', 'code', 'barcode']
