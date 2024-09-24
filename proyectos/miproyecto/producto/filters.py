import django_filters
from .models import Producto
from django import forms
from django.utils.translation import gettext_lazy as _

class ProductoFilter(django_filters.FilterSet):   
    nombre = django_filters.CharFilter(
        label=_("Nombre"),
        lookup_expr='icontains',
        widget = forms.TextInput(attrs={'class': 'form-control','placeholder':_("Ingresar el nombre del producto")})
    )
    class Meta:
        model=Producto
        fields=['nombre']