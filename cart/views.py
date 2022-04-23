from itertools import product
from pyexpat import model
from django.shortcuts import render
from django.views import generic
from .models import Product
# Create your views here.

class ProductListView(generic.ListView):
    template_name='product_list.html'
    queryset = Product.objects.all()

class ProductDetailView(generic.DetailView):
    model = Product
    template_name='cart/product_detail.html'
    #queryset = Product.objects.all()