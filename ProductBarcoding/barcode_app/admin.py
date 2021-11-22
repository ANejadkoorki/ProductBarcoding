from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Size)
class SizeModelAdmin(admin.ModelAdmin):
    """
        Size Model Admin settings
    """
    list_display = [
        'code',
        'name',
        'size_type',
    ]

    ordering = [
        'code',
    ]

    list_display_links = [
        'code',
        'name',
    ]

    list_filter = [
        'size_type'
    ]

    search_fields = [
        'code',
        'name',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
        Product Model Admin settings
    """

    list_display = [
        'code',
        'name',
        'barcode',
    ]

    ordering = [
        'code',
    ]

    list_display_links = [
        'code',
        'name',
    ]

    search_fields = [
        'barcode',
        'name',
    ]


@admin.register(MotherCategory, SecondCategory, ThirdCategory, Colour, Store)
class OtherModelsAdmin(admin.ModelAdmin):
    """
        Other Models Admin settings
    """

    list_display = [
        'code',
        'name',
    ]

    ordering = [
        'code',
    ]

    list_display_links = [
        'code',
        'name',
    ]

    search_fields = [
        'code',
        'name',
    ]
