# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/18 16:11
# File   : forms.py
# IDE    : PyCharm

from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
