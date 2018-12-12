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

class ServicesAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price_retail']
	list_filter = ['name', 'price_retail']
	prepopulated_fields = {'slug': ('name',)}

class ProductStockAdmin(admin.ModelAdmin):
	list_display = ['id', 'stock_start', 'stock_end', 'product', 'slug', 'available', 'description',]
	list_filter = ['stock_start', 'stock_end', 'product',]
	prepopulated_fields = {'slug': ('product',)}

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