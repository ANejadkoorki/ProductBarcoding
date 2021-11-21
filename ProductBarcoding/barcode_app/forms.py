from django import forms
from . import models


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = (
            'name',
            'mother_category',
            'second_category',
            'third_category',
            'colour',
            'size',
            'store',
        )
