from django.db import models
from django.db.models import F
# Create your models here.

CURRENCY_CHOICES = (
	('eur','EUR'),
	('usd','USD'),
	('uah', 'UAH')
	)

INTEREST_CHOICES = (
	(7,'7%'),
	(15,'15%'),
	(20,'20%'),
	(25,'25%'),


	)

class Rates(models.Model): #курс валют
	"""docstring for Rates"""
	usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
	eur = models.DecimalField(max_digits=10, decimal_places=2, blank=True)


class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name

class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE) #коталог продукта связь m2m
	name = models.CharField(max_length=400, db_index=True) #имя продукта
	vendor_code = models.CharField(max_length=200, db_index=True) #артикул или парт-номер
	slug = models.SlugField(max_length=400, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #картинка
	description = models.TextField(blank=True) #описание продукта

	currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True) #валюта
	price_purchase = models.DecimalField(max_digits=10, decimal_places=2, blank=True) #цена Закупки
	interest = models.DecimalField(max_digits=5, decimal_places=2, blank=True) #Процент
	price_retail = models.DecimalField(max_digits=10, decimal_places=2, blank=True) #розничная цена

	stock = models.PositiveIntegerField(blank=True) # Остатки
	available = models.BooleanField(default=True) # булево значение, указывающее, доступен ли продукт или нет
	created = models.DateTimeField(auto_now_add=True) # дата создания
	updated = models.DateTimeField(auto_now=True) #дата обновления

	
	# @classmethod
	# def price_uah(cls, price):
	# 	p = cls(price=price*28)
	# 	return p
		
	# def price_uah(self, price):
	# 	self.price=float(self.price)
	# 	return self.price*28.5


	class Meta:
		ordering = ('name',)
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		index_together = (('id', 'slug'),)


	def __str__(self):
		return self.name


class Services(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE) #коталог продукта связь m2m
	name = models.CharField(max_length=400, db_index=True) #имя продукта
	vendor_code = models.CharField(max_length=200, db_index=True) #артикул или парт-номер
	slug = models.SlugField(max_length=400, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #картинка
	description = models.TextField(blank=True) #описание продукта
	price_retail = models.DecimalField(max_digits=10, decimal_places=2)
	created = models.DateTimeField(auto_now_add=True) # дата создания
	updated = models.DateTimeField(auto_now=True) #дата обновления


	class Meta:
		ordering = ('name',)
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name


class ProductStock(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	available = models.BooleanField(default=True)
	slug = models.SlugField(max_length=400, db_index=True)	
	description = models.TextField(blank=True) #описание акции
	stock_start = models.DateTimeField(auto_now=False, auto_now_add=False,) # дата создания
	stock_end = models.DateTimeField(auto_now=False, auto_now_add=False,) # дата окончания

	class Meta:
		ordering = ('product',)
		verbose_name = 'Акция'
		verbose_name_plural = 'Акции'



class Order(models.Model): #сведений о клиенте
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	city = models.CharField(max_length=100)
	phone = models.CharField(max_length=250)
	new_post_office = models.CharField(max_length=20)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)


	class Meta:
		ordering = ('-created',)
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self): #получить общую стоимость товаров
		return sum(item.get_cost() for item in self.items.all())