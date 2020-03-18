# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/18 16:29
# File   : urls.py
# IDE    : PyCharm

from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]