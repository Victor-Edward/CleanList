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

class CustomerListView(ListView):
    model = Customer
    template_name = 'basic_app/customer_list.html'

class CreateCustomerView(CreateView):
    redirect_field_name = 'basic_app/customer_detail.html'
    form_class = CustomerForm
    model = Customer 

class CustomerDetailView (DetailView):
    model = Customer
    template_name = 'basic_app/customer_detail.html'

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_view')

class CustomerUpdateView(UpdateView):
    redirect_field_name = 'basic_app/customer_list.html'
    model = Customer
    fields = ['name', 'contact', 'address']