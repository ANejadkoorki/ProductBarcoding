from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

two_digit_categories_validator = RegexValidator(
    regex="^[0-9]{1}[1-9]{1}$",
    message="the code should be matched with the correct format : 01-99",
)
three_digit_categories_validator = RegexValidator(
    regex="^[0-9]{2}[1-9]{1}$",
    message="the code should be matched with the correct format : 001-999",
)


class MotherCategory(models.Model):
    """
        Mother category objects are made with this model.
    """
    code = models.CharField(
        verbose_name="mother category code",
        validators=[two_digit_categories_validator],
        unique=True,
        max_length=2,
    )
    name = models.CharField(
        verbose_name="mother category name",
        max_length=200,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ['name', 'code']


class SecondCategory(models.Model):
    """
        Second category objects are made with this model.
    """
    mother_category = models.ForeignKey(
        to=MotherCategory,
        on_delete=models.CASCADE,
    )
    code = models.CharField(
        verbose_name="second category code",
        validators=[two_digit_categories_validator],
        unique=True,
        max_length=2,
    )
    name = models.CharField(
        verbose_name="second category name",
        max_length=200,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ['name', 'code']


class ThirdCategory(models.Model):
    """
        Third category objects are made with this model.
    """
    second_category = models.ForeignKey(
        to=SecondCategory,
        on_delete=models.CASCADE,
    )
    code = models.CharField(
        verbose_name="third category code",
        validators=[three_digit_categories_validator],
        unique=True,
        max_length=3,
    )
    name = models.CharField(
        verbose_name="third category name",
        max_length=200,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ['name', 'code']
