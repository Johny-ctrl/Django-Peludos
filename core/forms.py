
from django import forms
from django.forms import ModelForm
from .models import ListaP

class ProductoForm(ModelForm):
    class Meta: 
        model=ListaP
        fields =['IdProducto', 'NombreP', 'Descripcion', 'Categoria', 'Precio']