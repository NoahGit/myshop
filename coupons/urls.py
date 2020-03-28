# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/28 17:12
# File   : urls.py
# IDE    : PyCharm

from django.urls import path
from . import views

app_name = 'coupons'

urlpatterns = [
    path('apply/', views.coupon_apply, name='apply'),
]