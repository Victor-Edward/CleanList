from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView, CreateView, UpdateView)
from .forms import CustomerForm, ProductForm
from .models import Customer, Product

class Index(TemplateView):
    template_name = 'index.html'

class ProductDetailView(DetailView):
    template_name = 'basic_app/product_detail.html'

class CreateProductView(CreateView):
    redirect_field_name = 'basic_app/product_detail.html'
    form_class = ProductForm
    model = Product

class ProductListView(ListView):
    model = Product
    template_name = 'basic_app/product_list.html'

class ProductUpdateView(UpdateView):
    redirect_field_name = 'basic_app/product_list.html'
    model = Product
    fields = ['name', 'product_type', 'brand', 'quantity']