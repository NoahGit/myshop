# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/21 15:26
# File   : urls.py
# IDE    : PyCharm

from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
]