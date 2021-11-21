from django.urls import path
from . import views

app_name = 'barcode_app'

urlpatterns = [
    path("", views.CreateProduct.as_view(), name='create-product')
]