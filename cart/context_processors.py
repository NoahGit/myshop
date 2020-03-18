# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/18 11:49
# File   : context_processors.py
# IDE    : PyCharm

from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}
