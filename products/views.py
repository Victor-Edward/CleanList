from django.views.generic import (TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView)
from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

class CreateProductView(CreateView):
    redirect_field_name = 'products/product_detail.html'
    form_class = ProductForm
    model = Product

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'

class ProductUpdateView(UpdateView):
    redirect_field_name = 'products/product_list.html'
    template_name = 'products/product_update_form.html'
    model = Product
    fields = ['name', 'product_type', 'brand', 'quantity', 'photo']

class ProductDeleteview(DeleteView):
    model = Product
    success_url = reverse_lazy('product_view')