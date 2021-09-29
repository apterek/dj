from shop.models import Product
from django import forms


class StatusProduct(forms.Form):
    choise = forms.ChoiceField(choices=((1, "router"), (2, "switch")),
                               label="", initial='', widget=forms.Select(), required=True)
