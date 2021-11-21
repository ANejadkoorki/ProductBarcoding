from django.db import models
from django.core.validators import RegexValidator

two_digit_validator = RegexValidator(
    regex="^[0-9]{1}[1-9]{1}$",
    message="the code should be matched with the correct format : 01-99",
)
four_digit_validator = RegexValidator(
    regex="^[0-9]{3}[1-9]{1}$",
    message="the code should be matched with the correct format : 0001-9999",
)


class Store(models.Model):
    code = models.CharField(
        verbose_name="store code",
        validators=[four_digit_validator],
        unique=True,
        max_length=4,
    )
    name = models.CharField(
        verbose_name="store name",
        max_length=200,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ['name', 'code']


class Size(models.Model):
    TYPE_CHOICES = [
        ('C', 'CLOTHING'),
        ('W', 'WEIGHT'),
        ('D', 'DIMENSIONAL'),
    ]
    code = models.CharField(
        verbose_name="size code",
        validators=[two_digit_validator],
        max_length=2,
    )
    size_type = models.CharField(
        verbose_name="size type",
        choices=TYPE_CHOICES,
        default="CLOTHING",
        max_length=50,
    )
    name = models.CharField(
        verbose_name="size name",
        max_length=200,
    )

    def __str__(self):
        return f"{self.size_type}: {self.name}"

    class Meta:
        unique_together = ['code', 'size_type', 'name']


class Colour(models.Model):
    code = models.CharField(
        verbose_name="colour code",
        validators=[two_digit_validator],
        unique=True,
        max_length=2,
    )
    name = models.CharField(
        verbose_name="colour name",
        max_length=200,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ['name', 'code']

# class ClothingSize(models.Model):
#     code = models.CharField(
#         verbose_name="clothing size code",
#         validators=[two_digit_validator],
#         unique=True,
#     )
#     name = models.CharField(
#         verbose_name="clothing size name",
#     )
#
#     class Meta:
#         unique_together = ['name', 'code']
#
#
# class WeightSize(models.Model):
#     code = models.CharField(
#         verbose_name="weight size code",
#         validators=[two_digit_validator],
#         unique=True,
#     )
#     name = models.CharField(
#         verbose_name="weight size name",
#     )
#
#     class Meta:
#         unique_together = ['name', 'code']


# class DimensionalSize(models.Model):
#     code = models.CharField(
#         verbose_name="dimensional size code",
#         validators=[two_digit_validator],
#         unique=True,
#     )
#     name = models.CharField(
#         verbose_name="dimensional size name",
#     )
#
#     class Meta:
#         unique_together = ['name', 'code']
