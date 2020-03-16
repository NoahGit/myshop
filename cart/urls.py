# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/16 15:31
# File   : urls.py
# IDE    : PyCharm

from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
