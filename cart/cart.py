# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2020/3/16 10:36
# File   : cart.py
# IDE    : PyCharm

from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        :param request:
        """
        # 存储当前会话
        self.session = request.session
        # 从当前会话中获取购物车
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        :param product:
        :param quantity:
        :param update_quantity:
        :return:
        """
        # JSON只支持字符串，所以将product.id格式化为字符串格式
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved将会话标记为“修改”，以确保它被保存
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart
        :param product:
        :return:
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.遍历购物车中的商品并从数据库中获取产品。
        :return:
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart获取产品对象并将它们添加到购物车中
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        :return:
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()