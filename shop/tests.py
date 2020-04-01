from django.test import TestCase
from shop.models import Product
from shop.recommender import Recommender

# Create your tests here.
red_wine_1 = Product.objects.get(name='法国进口红酒 西夫拉姆AOP干红葡萄酒')
red_wine_2 = Product.objects.get(name='法国进口红酒 拉菲（LAFITE）珍藏波尔多法定产区干红葡萄酒750ml')
red_wine_3 = Product.objects.get(name='法国进口红酒怡园干红2018年份普通餐酒橡木桶陈酿750ML')
red_wine_4 = Product.objects.get(name='英国进口红酒 贝灵哲酒庄红葡萄酒 贝灵哲创始者黑皮诺红葡萄酒750ml')

r = Recommender()
r.products_bought([red_wine_1, red_wine_2])
r.products_bought([red_wine_1, red_wine_3])
r.products_bought([red_wine_2, red_wine_1, red_wine_4])
r.products_bought([red_wine_3, red_wine_4])
r.products_bought([red_wine_1, red_wine_4])
r.products_bought([red_wine_2, red_wine_3])

r.suggest_products_for([red_wine_1])
r.suggest_products_for([red_wine_1, red_wine_2])
r.suggest_products_for([red_wine_3, red_wine_2])
r.suggest_products_for([red_wine_4, red_wine_1])