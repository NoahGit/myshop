# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/28 13:32
# File   : forms.py
# IDE    : PyCharm

from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField()