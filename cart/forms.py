# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/16 14:12
# File   : forms.py
# IDE    : PyCharm

from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
