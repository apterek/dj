from shop.models import Product
from django import forms
from shop.models import STATUS_CHOICES, ORDER_BY_CHOICES


class FormStatus(forms.Form):

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )

    cost__gt = forms.IntegerField(
        min_value=0,
        label="Price Min",
        widget=forms.TextInput(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )

    cost__lt = forms.IntegerField(
        min_value=0,
        label="Price Max",
        widget=forms.TextInput(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )

    order_by = forms.ChoiceField(
        choices=ORDER_BY_CHOICES,
        widget=forms.Select(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )


class FilterDate(forms.Form):
    filter_by_date = forms.ChoiceField(
        choices=(("NEW_FIRST", "new first"), ("OLD_AT_FIRST", "old at first")),
        widget=forms.Select(attrs={"class": "ml-1 mr-3"}),
        required=False,
    )
