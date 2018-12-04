from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
	def __init__(self, request):
	# Инициализация корзины пользователя
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
		# Сохраняем корзину пользователя в сессию
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart


	def add(self, product, quantity=1, update_quantity=False):
		"""
		Добавить продукт в корзину или обновить его количество.
		"""
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity': 0,
									 'price_uah': str(product.price_uah)}
		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save()

		def save(self):
		# Обновление сессии cart
			self.session[settings.CART_SESSION_ID] = self.cart
			# Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
			self.session.modified = True

 # Сохранение данных в сессию
	def save(self):
		self.session[settings.CART_SESSION_ID] = self.cart
		# Указываем, что сессия изменена
		self.session.modified = True

	def remove(self, product):
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	# Итерация по товарам
	def __iter__(self):
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		for product in products:
			self.cart[str(product.id)]['product'] = product

		for item in self.cart.values():
			item['price_uah'] = Decimal(item['price_uah'])
			item['total_price_uah'] = item['price_uah'] * item['quantity']
			yield item


	# Количество товаров
	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price_uah(self):
		return sum(Decimal(item['price_uah']) * item['quantity'] for item in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True

	@property
	def cupon(self):
		if self.cupon_id:
			return Cupon.objects.get(id=self.cupon_id)
		return None

	def get_discount(self):
		if self.cupon:
			return (self.cupon.discount / Decimal('100')) * self.get_total_price_uah()
		return Decimal('0')

	def get_total_price_uah_after_discount(self):
		return self.get_total_price_uah() - self.get_discount() 