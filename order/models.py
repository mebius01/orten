from django.db import models
from shop.models import Product

PAY_CHOICES = (
	('Наличные','Наличные'),
	('Безналичный расчет', 'Безналичный расчет'),
	)

DELIVERY_CHOICES = (
	('Самовывоз','Самовывоз'),
	('Новой Почтой','Новой Почтой'),
	)

class Order(models.Model):
	delivery_method = models.CharField(max_length=50, choices=DELIVERY_CHOICES, verbose_name='Спопсоб доставки', default=True)
	pay_method = models.CharField(max_length=50, choices=PAY_CHOICES, verbose_name='Спопсоб оплаты', default=True)

	last_name = models.CharField(verbose_name='Фамилия', max_length=50)
	first_name = models.CharField(verbose_name='Имя', max_length=50)
	sur_name = models.CharField(verbose_name='Отчесво', max_length=50)
	city = models.CharField(verbose_name='Город', max_length=100)
	department_np = models.CharField(verbose_name='НП №', max_length=300)

	mobile_phone = models.CharField(max_length=15, verbose_name='Телефон')
	email = models.EmailField(verbose_name='Email')
	note_text =  models.TextField(blank=True, max_length=512, verbose_name='Дополнения, пожелания, заметки')

	created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
	paid = models.BooleanField(verbose_name='Оплачен', default=False)

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return 'Заказ: {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity
