# import dramatiq
# from celery import task
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from .models import Order

# @task
# def order_created(order_id):
# 	"""
# 	Отправка Email сообщения о создании покупке
# 	"""

# 	order = Order.objects.get(id=order_id)
# 	subject = 'Заказ c номером {}'.format(order.id)
# 	message = render_to_string('email/order_client.html', {'order': order})
# 	send_mail(subject, message, 'consmebius@gmail.com', [order.email], html_message=message)
# 	order = Order.objects.get(id=order_id)
# 	subject = 'ЗАКАЗ НА САЙТЕ №{}'.format(order.id)
# 	message = render_to_string('email/order_admin.html', {'order': order})
# 	send_mail(subject, message, 'consmebius@gmail.com', ['consmebius@gmail.com'], html_message=message)

import dramatiq
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Order
from django.conf import settings

admin = str(settings.ADMINS[0][1])
print(admin)

@dramatiq.actor
def email_customer(order_id):
	order = Order.objects.get(id=order_id)
	subject = 'Заказ c номером {}'.format(order.id)
	message = render_to_string('email/order_client.html', {'order': order})
	send_mail(subject, message, admin , [order.email], html_message=message)
	order = Order.objects.get(id=order_id)
	subject = 'ЗАКАЗ НА САЙТЕ №{}'.format(order.id)
	message = render_to_string('email/order_admin.html', {'order': order})
	send_mail(subject, message, admin, [admin], html_message=message)