from celery import task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Order

@task
def order_created(order_id):
	"""
	Отправка Email сообщения о создании покупке
	"""

	order = Order.objects.get(id=order_id)
	subject = 'Заказ c номером {}'.format(order.id)
	message = render_to_string('email/order_mail.html', {'order': order})
	mail_send = send_mail(subject, message, 'consmebius@gmail.com', [order.email], html_message=message)
	return mail_send

