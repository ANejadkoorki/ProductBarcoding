from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from . import forms, models
from django.views.generic import CreateView


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
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
        cleaned_data = form.cleaned_data

        prod_last_object = models.Product.objects.last()
        if prod_last_object:
            last_prod_code = int(prod_last_object.code)
            new_prod_code_int = last_prod_code + 1
            new_prod_code = str(new_prod_code_int).zfill(5)
            new_obj = models.Product.objects.create(
                code=new_prod_code,
                mother_category=cleaned_data.get('mother_category'),
                second_category=cleaned_data.get('second_category'),
                third_category=cleaned_data.get('third_category'),
                colour=cleaned_data.get('colour'),
                size=cleaned_data.get('size'),
                store=cleaned_data.get('store'),
                name=cleaned_data.get('name'),
            )
            messages.success(request=self.request,
                             message=f"Product has been saved successfully with barcode: {new_obj.get_barcode()}")
            return redirect('barcode_app:create-product')
        else:
            new_obj = models.Product.objects.create(
                code='00001',
                mother_category=cleaned_data.get('mother_category'),
                second_category=cleaned_data.get('second_category'),
                third_category=cleaned_data.get('third_category'),
                colour=cleaned_data.get('colour'),
                size=cleaned_data.get('size'),
                store=cleaned_data.get('store'),
                name=cleaned_data.get('name'),
            )
            messages.success(request=self.request,
                             message=f"Product has been saved successfully with barcode: {new_obj.get_barcode()}")
            return redirect('barcode_app:create-product')

