from django.shortcuts import render
from . import forms, models
from django.views.generic import CreateView


# Create your views here.


class CreateProduct(CreateView):
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
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        form = forms.CreateProductForm()

        return render(
            request,
            template_name="barcode_app/base_page.html",
            context={
                'form': form,
            },
        )

    def form_valid(self, form):
        pass
