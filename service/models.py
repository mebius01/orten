from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
from shop.models import Product

# Create your models here.
class Category_Services(MPTTModel):
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
		verbose_name = 'Категория Сервис'
		verbose_name_plural = 'Категории Сервис'


	def get_absolute_url(self):
		return '/'.join([x['slug'] for x in self.get_ancestors(include_self=True).values()])

	def get_anc(self):
		return self.get_ancestors(include_self=True)


	def __str__(self):
		return self.name

class Services(models.Model):
	category = models.ForeignKey(Category_Services,related_name='services', on_delete=models.CASCADE) #коталог продукта связь
	name = models.CharField(max_length=400, db_index=True) #имя продукта
	accessories = models.ManyToManyField(Product, related_name="services_acces", blank=True)
	vendor_code = models.CharField(max_length=200, blank=True) #артикул или парт-номер
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