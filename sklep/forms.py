from django import forms

from .models import Product


"""class ProductForm(forms.ModelForm):
    class Meta:
        model  = Product
        fields = [
            'title',
            'quantity_in_store',
            'price',
            'description'
        ]
"""


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tytuł",
                "rows": 1,
                "cols": 100
                }
            )
        )
    quantity_in_store = forms.IntegerField(
        label='ilość produktów',
        initial=1
        )
    price = forms.DecimalField(
        label='cena produktu'
        )
    description = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Opis produktu",
                "class": "new-class-name two",
                "rows": 35,
                "cols": 100
                }
            )
        )

    class Meta:
        model  = Product
        fields = [
            'title',
            'quantity_in_store',
            'price',
            'description'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "My" in title:  # title must have "My"
            raise forms.ValidationError('This is not a valid title, must start with \'My\'')
        return title

    def clean_quantity_in_store(self, *args, **kwargs):
        quantity_in_store = self.cleaned_data.get('quantity_in_store')
        if quantity_in_store < 1:
            raise forms.ValidationError('This is not a valid quantity')
        return quantity_in_store

    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get('price')
        if price < 0.10:
            raise forms.ValidationError('This is not a valid price')
        return price


# RawProductForm to drugi sposób:

class RawProductForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tytuł",
                "rows": 1,
                "cols": 100
                }
            )
        )
    quantity_in_store = forms.IntegerField(
        label='ilość produktów',
        initial=1
        )
    price = forms.DecimalField(
        label='cena produktu'
        )
    description = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Opis produktu",
                "class": "new-class-name two",
                "rows": 35,
                "cols": 100
                }
            )
        )