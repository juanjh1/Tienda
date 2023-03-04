from django import forms
from .models import Color, Talla, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = ('name', 'category', 'desc', 'image', 'cantidad', 'price')


class TallaColorForm(forms.Form):
    tallas = forms.ModelMultipleChoiceField(queryset=Talla.objects.all(),
                                            widget=forms.CheckboxSelectMultiple())
    colores = forms.ModelMultipleChoiceField(queryset=Color.objects.all(),
                                             widget=forms.CheckboxSelectMultiple())
