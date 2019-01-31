from django.db import models
from django.db.models import F
from decimal import *
import django_filters


# Create your models here.

from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager

CURRENCY_CHOICES = (
	('eur','EUR'),
	('usd','USD'),
	('uah', 'UAH'),
	)

SALER_CHOICES = (
	('esko','esko'),
	('softcom','softcom'),
	('megateid', 'megateid'),
	('baden', 'baden'),
	('Konica', 'Konica'),

	)


INTEREST_CHOICES = (
	(Decimal("0.07"), '7%'),
	(Decimal("0.15"), '15%'),
	(Decimal("0.20"), '20%'),
	(Decimal("0.25"), '25%'),
	(Decimal("0.30"), '30%'),



	)

# class Rates(models.Model): #курс валют
# 	"""docstring for Rates"""
# 	usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
# 	eur = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

# 	class Meta:
# 		verbose_name = 'Курс Валют'
# 		verbose_name_plural = 'Курсы Валют'


class Category(MPTTModel):
	name = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True) #описание Категории
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


	class MPTTMeta:
		order_insertion_by = ['name']


	class Meta:
		unique_together = ('parent', 'slug',)
		ordering = ('tree_id', 'name',)
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


	def get_absolute_url(self):
		return '/'.join([x['slug'] for x in self.get_ancestors(include_self=True).values()])

	def get_anc(self):
		return self.get_ancestors(include_self=True)


	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(Category,related_name='product', on_delete=models.CASCADE, help_text='Каталог товара (расходные материалы, компьютеры и комплетующие и т д)') #коталог продукта связь m2m
	name = models.CharField(max_length=400, db_index=True, help_text='Название товара') #имя продукта
	# name_f_k = models.ForeignKey(Product.name, on_delete=models.CASCADE, help_text='Каталог товара (расходные материалы, компьютеры и комплетующие и т д)')
	# saler =  models.CharField(max_length=25, choices=SALER_CHOICES, blank=True, help_text='Поставщик')
	accessories = models.ManyToManyField("self", blank=True)
	vendor_code = models.CharField(max_length=200, db_index=True, help_text='Артикул, парт номер') #артикул или парт-номер
	vendor = models.CharField(max_length=200, blank=True, help_text='Производитель') # Производитель
	type_product = models.CharField(max_length=200, blank=True, help_text='Тип товара')
	
	slug = models.SlugField(max_length=400, help_text='')
	
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, help_text='') #картинка
	
	keywords =  models.TextField(blank=True, help_text='Ключивые слова (тонер, материнская плата, пружина)')#краткое описание продукта
	description = models.TextField(blank=True, help_text='Описание товара') #описание продукта
	tags = TaggableManager(through=None, blank=True, help_text = 'Список тегов, разделенных запятыми')

	# currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True, help_text='Валюта входа') #валюта
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, help_text='Цена входящая') #цена Закупки
	interest = models.DecimalField(max_digits=5, decimal_places=2, blank=True, choices=INTEREST_CHOICES, null=True, help_text='Процент, накрутка') #Процент
	
	stock = models.PositiveIntegerField(blank=True, help_text='Остатоки') # Остатки
	available = models.BooleanField(default=True, help_text='Доступен ли к заказу') # булево значение, указывающее, доступен ли продукт или нет
	created = models.DateTimeField(auto_now_add=True, help_text='дата создания') # дата создания
	updated = models.DateTimeField(auto_now=True, help_text='дата обновления') #дата обновления

	# @property
	# def price_uah(self):
	# 	rates_usd=float(Rates.objects.get(id=1).usd)
	# 	rates_eur=float(Rates.objects.get(id=1).eur)
	# 	self.price_purchase=float(self.price_purchase)
	# 	self.interest=float(self.interest)
	# 	if self.saler == 'softcom':
	# 		a = ((self.price_purchase*self.interest)+self.price_purchase)*rates_usd
	# 		return format(a, '.2f')
	# 	if self.saler == 'esko':
	# 		a = ((self.price_purchase*self.interest)+self.price_purchase)*rates_usd
	# 		return format(a, '.2f')
	# 	if self.saler == 'megateid':
	# 		a = ((self.price_purchase*self.interest)+self.price_purchase)*rates_usd
	# 		return format(a, '.2f')
	# 	if self.saler == 'Konica':
	# 		a = self.price_purchase*rates_eur
	# 		return format(a, '.2f')
	# 	if self.saler == 'baden':
	# 		a= self.price_purchase
	# 		return format(a, '.2f')

	class Meta:
		ordering = ('name',)
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		index_together = (('id', 'slug'),)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return (self.category.get_absolute_url()+'/'+self.slug)




class Services(models.Model):
	category = models.ForeignKey(Category,related_name='services', on_delete=models.CASCADE) #коталог продукта связь
	name = models.CharField(max_length=400, db_index=True) #имя продукта
	accessories = models.ManyToManyField(Product, blank=True)
	vendor_code = models.CharField(max_length=200, blank=True) #артикул или парт-номер
	vendor = models.CharField(max_length=200, blank=True, help_text='Производитель') # Производитель
	vendor_model = models.CharField(max_length=200, blank=True, help_text='Модель')
	slug = models.SlugField(max_length=400, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #картинка
	description = models.TextField(blank=True) #описание продукта
	price = models.DecimalField(max_digits=10, decimal_places=2)
	created = models.DateTimeField(auto_now_add=True) # дата создания
	updated = models.DateTimeField(auto_now=True) #дата обновления



	class Meta:
		ordering = ('name',)
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return (self.category.get_absolute_url()+'/'+self.slug)


class ProductStock(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	discount_percent =  models.DecimalField(max_digits=5, decimal_places=2, blank=True, choices=INTEREST_CHOICES, null=True, help_text='Процент скидка') #Процент)
	available = models.BooleanField(default=True)
	slug = models.SlugField(max_length=400, db_index=True)	
	description = models.TextField(blank=True) #описание акции
	stock_start = models.DateTimeField(auto_now=False, auto_now_add=False,) # дата создания
	stock_end = models.DateTimeField(auto_now=False, auto_now_add=False,) # дата окончания

	@property
	def discount(self):
		product_price_uah=float(self.product.price)
		discount_percent=float(self.discount_percent)
		return product_price_uah - (product_price_uah*discount_percent)



	class Meta:
		ordering = ('product',)
		verbose_name = 'Акция'
		verbose_name_plural = 'Акции'