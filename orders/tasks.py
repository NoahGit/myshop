from celery import Celery, task
from django.core.mail import send_mail
from .models import Order

app = Celery('tasks', broker='amqp://guest@localhost//')


@app.task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.任务，在成功创建订单时发送电子邮件通知。
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {}, \n\nYou have successfully placed an order.' \
              ' your order id is {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'xiangjiaotuobei@163.com', [order.email])
    return mail_sent
