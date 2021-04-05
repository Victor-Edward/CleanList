from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'contact', 'address', 'photo')
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nome"
        self.fields['contact'].label = "Contato"
        self.fields['address'].label = "Endereço"
        self.fields['photo'].label = "Foto"

