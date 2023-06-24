from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.
class IndexView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "product/index.html"