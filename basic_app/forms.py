from django import forms
from .models import Customer, Product

class CustomerForm(forms.ModelForm):

    class meta():
        model = Customer
        fields = ('nome', 'contato', 'endereço')

class ProductForm(forms.ModelForm):

    class meta():
        model = Product
        fields = ('nome', 'tipo_de_produto', 'quantidade')

