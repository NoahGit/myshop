import os
from celery import Celery

# set the default Django settings module for the 'celery' program.为“celery”程序设置默认的Django设置模块。
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()