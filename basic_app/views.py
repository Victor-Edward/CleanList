from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView)
from .forms import CustomerForm, ProductForm
from .models import Customer, Product
from django.urls import reverse_lazy

class Index(TemplateView):
    template_name = 'index.html'

class ProductDetailView(DetailView):
    model = Product
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

class ProductDeleteview(DeleteView):
    model = Product
    success_url = reverse_lazy('product_view')