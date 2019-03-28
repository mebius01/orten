from django.db import models
# from django.db.models import F
from decimal import *
import django_filters
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.contrib.flatpages.models import FlatPage
from datetime import datetime 

class Category(MPTTModel):
	name = models.CharField(max_length=200, db_index=True, unique=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)
	image = models.ImageField(upload_to='category/', blank=True)
	description = models.TextField(blank=True)
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

FORMAT_CHOICES = (
	('A0', 'A0'),
	('A1', 'A1'),
	('A2', 'A2'),
	('A3', 'A3'),
	('A4', 'A4'),
	('A5', 'A5'),
	('A6', 'A6'),
	('A7', 'A7'),
	('A8', 'A8'),
	('A9', 'A9'),
	('A10', 'A10'),
	)

COLOR_CHOICES = (
	('BW', 'BW'),
	('Color', 'Color'),
	)

INTEREST_CHOICES = (
	(Decimal("0.03"), '3%'),
	(Decimal("0.04"), '4%'),
	(Decimal("0.05"), '5%'),
	(Decimal("0.06"), '6%'),
	(Decimal("0.07"), '7%'),
	(Decimal("0.08"), '8%'),
	(Decimal("0.09"), '9%'),
	(Decimal("0.10"), '10%'),
	(Decimal("0.11"), '11%'),
	(Decimal("0.12"), '12%'),
	(Decimal("0.13"), '13%'),
	(Decimal("0.14"), '14%'),
	(Decimal("0.15"), '15%'),
	(Decimal("0.16"), '16%'),
	(Decimal("0.17"), '17%'),
	(Decimal("0.18"), '18%'),
	(Decimal("0.19"), '19%'),
	(Decimal("0.20"), '20%'),
	(Decimal("0.21"), '21%'),
	(Decimal("0.22"), '22%'),
	(Decimal("0.23"), '23%'),
	(Decimal("0.24"), '24%'),
	(Decimal("0.25"), '25%'),
	(Decimal("0.26"), '26%'),
	(Decimal("0.27"), '27%'),
	(Decimal("0.28"), '28%'),
	(Decimal("0.30"), '30%'),
	)

class Product(models.Model):
	category = models.ForeignKey(Category,related_name='product', on_delete=models.CASCADE, help_text='Каталог товара (расходные материалы, компьютеры и комплетующие и т д)') #коталог продукта связь m2m
	name = models.CharField(max_length=400, db_index=True, help_text='Название товара') #имя продукта
	slug = models.SlugField(max_length=400, help_text='')
	provider = models.CharField(max_length=20, help_text='Поставщик')
	accessories = models.ManyToManyField("self", blank=True)
	vendor_code = models.CharField(max_length=200, db_index=True, help_text='Артикул, парт номер') #артикул или парт-номер
	vendor = models.CharField(max_length=200, blank=True, help_text='Производитель') # Производитель
	image = models.ImageField(upload_to='product/', blank=True, help_text='') #картинка

	format_fild = models.CharField(max_length=50, blank=True, choices=FORMAT_CHOICES, help_text='A3,A4')
	color_fild = models.CharField(max_length=50, blank=True, choices=COLOR_CHOICES, help_text='BW, Color')
	specifications = RichTextField(blank=True, help_text='Характеристики товара')
	type_product = models.CharField(max_length=200, blank=True, help_text='Тип товара')
	description = models.TextField(blank=True, help_text='Описание товара') #описание продукта
	tags = TaggableManager(through=None, blank=True, help_text = 'Список тегов, разделенных запятыми')
	# test_fild = models.CharField(max_length=200, blank=True, help_text='Тстовое поле на ошибку') # django.db.utils.ProgrammingError: ОШИБКА:  столбец shop_product.test_fild не существует
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, help_text='Цена входящая') #цена Закупки
	stock = models.PositiveIntegerField(blank=True, help_text='Остатоки') # Остатки
	available = models.BooleanField(default=True, help_text='Доступен ли к заказу') # булево значение, указывающее, доступен ли продукт или нет

	date_start_action = models.DateTimeField(auto_now=False, blank=True, auto_now_add=False,) # дата создания
	date_end_action = models.DateTimeField(auto_now=False, blank=True, auto_now_add=False,) # дата окончания
	action = models.BooleanField(default=False, help_text='Акции')
	# action_end = models.DateTimeField(auto_now=False, auto_now_add=False, help_text='Дата окончания акции',) # дата окончания
	discount =  models.DecimalField(max_digits=10,default=Decimal("0.00"), decimal_places=2, blank=True,  help_text='Цена со скидкой') #Процент)
	created = models.DateTimeField(auto_now_add=True, help_text='дата создания') # дата создания
	updated = models.DateTimeField(auto_now=True, help_text='дата обновления') #дата обновления
	def end_action(self):
		if self.action:
			if datetime.now() > self.date_end_action:
				self.action = False


	# date_start_action = models.DateTimeField(auto_now=False, blank=True, auto_now_add=False,) # дата создания
	# date_end_action = models.DateTimeField(auto_now=False, blank=True, auto_now_add=False,) # дата окончания

	class Meta:
		ordering = ('name',)
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		index_together = (('id', 'slug'),)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return ('shop/'+self.slug)

class Services(models.Model):
	category = models.ForeignKey(Category,related_name='services', on_delete=models.CASCADE) #коталог продукта связь
	name = models.CharField(max_length=400, db_index=True) #имя продукта
	slug = models.SlugField(max_length=400, db_index=True)
	accessories = models.ManyToManyField(Product, blank=True)
	vendor_code = models.CharField(max_length=200, blank=True) #артикул или парт-номер
	vendor = models.CharField(max_length=200, blank=True, help_text='Производитель') # Производитель
	vendor_model = models.CharField(max_length=200, blank=True, help_text='Модель')
	image = models.ImageField(upload_to='service/', blank=True) #картинка
	description = models.TextField(blank=True)
	keywords= models.TextField(blank=True, help_text='Ключивые слова')
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
		return ('service/'+self.slug)

class Polygraphy(models.Model):
	# category = models.ForeignKey(Category,related_name='polygraphy', on_delete=models.CASCADE) #коталог продукта связь
	slug = models.SlugField(max_length=400, default='True', help_text='')
	flatpage = models.OneToOneField(FlatPage, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='polygraphy/', blank=True) #картинка
	description = models.TextField(blank=True)
	keywords= models.TextField(blank=True, help_text='Ключивые слова')

	class Meta:
		verbose_name = 'Полиграфия'
		verbose_name_plural = 'Полиграфия'

	def __str__(self):
		return self.flatpage.title


# class ProductStock(models.Model):
# 	product = models.ForeignKey(Product, on_delete=models.CASCADE)
# 	slug = models.SlugField(max_length=400, db_index=True)	
# 	description = models.TextField(blank=True) #описание акции
# 	stock_start = models.DateTimeField(auto_now=False, blank=True, auto_now_add=False,) # дата создания
# 	stock_end = models.DateTimeField(auto_now=False, blank=True, auto_now_add=False,) # дата окончания

	# @property
	# def discount(self):
	# 	product_price_uah=float(self.product.price)
	# 	discount_percent=float(self.discount_percent)
	# 	return product_price_uah - (product_price_uah*discount_percent)

	# class Meta:
	# 	ordering = ('product',)
	# 	verbose_name = 'Акция'
	# 	verbose_name_plural = 'Акции'
