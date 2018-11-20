from django.contrib import admin
from .models import Category, Product, Services, Rates, ProductStock
from mptt.admin import MPTTModelAdmin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class RatesAdmin(admin.ModelAdmin):
	list_display = ['id', 'usd', 'eur',]
	list_editable = ['usd', 'eur']

class CategoryAdmin(MPTTModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	mptt_level_indent = 30
# class GenreAdmin(admin.ModelAdmin):
# 	list_display = ['name', 'slug']
# 	prepopulated_fields = {'slug': ('name',)}


# class ProductAdmin(admin.ModelAdmin):
# 	list_display = ['name', 'slug', 'saler', 'price_purchase', 'price_uah', 'currency', 'interest', 'price_retail', 'stock', 'available', 'updated']
# 	list_filter = ['available', 'created', 'updated']
# 	list_editable = ['price_purchase', 'currency', 'interest', 'price_retail', 'stock', 'available']
# 	prepopulated_fields = {'slug': ('name',)}


class ServicesAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price_retail']
	list_filter = ['name', 'price_retail']
	prepopulated_fields = {'slug': ('name',)}

class ProductStockAdmin(admin.ModelAdmin):
	list_display = ['id', 'stock_start', 'stock_end', 'product', 'slug', 'available', 'description',]
	list_filter = ['stock_start', 'stock_end', 'product',]
	prepopulated_fields = {'slug': ('product',)}

# category = models.ForeignKey(Category, on_delete=models.CASCADE) #коталог продукта связь m2m
# name = models.CharField(max_length=400, db_index=True) #имя продукта
# saler =  models.CharField(max_length=25, choices=SALER_CHOICES, blank=True)
# vendor_code = models.CharField(max_length=200, db_index=True) #артикул или парт-номер
# vendor = models.CharField(max_length=200, blank=True) # Производитель
# slug = models.SlugField(max_length=400, db_index=True)
# image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #картинка
# keywords =  models.TextField(blank=True)#краткое описание продукта
# description = models.TextField(blank=True) #описание продукта

# currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True) #валюта
# price_purchase = models.DecimalField(max_digits=10, decimal_places=2, blank=True) #цена Закупки
# interest = models.DecimalField(max_digits=5, decimal_places=2, blank=True, choices=INTEREST_CHOICES, null=True) #Процент
# price_retail = models.DecimalField(max_digits=10, decimal_places=2, blank=True) #розничная цена

# stock = models.PositiveIntegerField(blank=True) # Остатки
# available = models.BooleanField(default=True) # булево значение, указывающее, доступен ли продукт или нет
# created = models.DateTimeField(auto_now_add=True) # дата создания
# updated = models.DateTimeField(auto_now=True) #дата обновления

class ProductAdmin(ImportExportModelAdmin):
	list_display = ['name', 'slug', 'saler', 'price_purchase', 'price_uah', 'currency', 'interest', 'stock', 'available', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price_purchase', 'currency', 'interest', 'stock', 'available']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin,)
admin.site.register(Product, ProductAdmin,)
admin.site.register(Services, ServicesAdmin,)
admin.site.register(Rates, RatesAdmin,)
admin.site.register(ProductStock, ProductStockAdmin,)