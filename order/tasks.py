from celery import task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Order

@task
def order_created(order_id):
	"""
	Отправка Email сообщения о создании покупке
	"""
	# order = Order.objects.get(id=order_id)
	# subject = 'Заказ c номером {}'.format(order.id)
	# message = 'Дорогой, {}, вы успешно сделали заказ.'.format(order.first_name)+ '\n' + \
	# 'Номер вашего заказа {}'.format(order.id) + '\n' + \
	# 'Ваши попкупки {}, в количесве {} = {}'.format([x.product.name for x in order.items.all()], [x.quantity for x in order.items.all()], [x.get_cost() for x in order.items.all()])+ '\n' + \
	# 'Сумма вашего заказа {}'.format(order.get_total_cost())
	# mail_send = send_mail(subject, message, 'consmebius@gmail.com', [order.email])
	# return mail_send

	order = Order.objects.get(id=order_id)
	subject = 'Заказ c номером {}'.format(order.id)
	message = render_to_string('email/order_mail.html', {'order': order})
	mail_send = send_mail(subject, message, 'consmebius@gmail.com', [order.email], html_message=message)
	return mail_send