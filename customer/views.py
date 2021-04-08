from django.views.generic import (TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView)
from .forms import CustomerForm
from .models import Customer
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from .private import googleapi_key

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'

class CreateCustomerView(CreateView):
    redirect_field_name = 'customer/customer_detail.html'
    form_class = CustomerForm
    model = Customer 

class CustomerDetailView (DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context['googleapi_key'] = googleapi_key
        return context

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_view')

class CustomerUpdateView(UpdateView):
    redirect_field_name = 'customer/customer_list.html'
    template_name = 'customer/customer_update_form.html'
    model = Customer
    fields = ['name', 'contact', 'address', 'photo']