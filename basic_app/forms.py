from django import forms
from .models import Customer, Product

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'contact', 'address')
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nome"
        self.fields['contact'].label = "Contato"
        self.fields['address'].label = "Endereço"

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'product_type', 'brand', 'quantity')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nome"
        self.fields['product_type'].label = "Tipo de produto"
        self.fields['brand'].label = "Marca"
        self.fields['quantity'].label = "Quantidade em estoque"

