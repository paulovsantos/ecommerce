from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from ecommerce.models import Product


def home(request):
    products = Product.objects.all()
    return render(
        request=request, template_name="products.html", context={"products": products}
    )


""" 
class ListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
"""
