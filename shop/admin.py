from django.contrib import admin
from .models import Category, Product, ProductStock, Services #Rates, 
from mptt.admin import MPTTModelAdmin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from import_export import resources

# class ProductResource(resources.ModelResource):

# 	class Meta:
# 		model = Product
		# fields = ['id', 'category', 'name', 'vendor', 'vendor_code', 'slug', 'price', 'interest', 'stock', 'available',]

# class RatesAdmin(admin.ModelAdmin):
# 	list_display = ['id', 'usd', 'eur',]
# 	list_editable = ['usd', 'eur']

class CategoryAdmin(MPTTModelAdmin):
	list_display = ['name', 'id', 'slug']
	prepopulated_fields = {'slug': ('name',)}
	mptt_level_indent = 30

class ServicesAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price']
	list_filter = ['name', 'price']
	prepopulated_fields = {'slug': ('name',)}

class ProductStockAdmin(admin.ModelAdmin):
	list_display = ['id', 'stock_start', 'stock_end', 'product', 'slug', 'available', 'description',]
	list_filter = ['stock_start', 'stock_end', 'product',]
	prepopulated_fields = {'slug': ('product',)}

class ProductAdmin(ImportExportModelAdmin):
	# resource_class = ProductResource
	search_fields = ['name',]
	list_display = ['name', 'id', 'slug', 'price', 'interest', 'stock', 'available', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'interest', 'stock', 'available']
	prepopulated_fields = {'slug': ('name',)}

class ProductResource(resources.ModelResource):
	class Meta:
		model = Product


admin.site.register(Category, CategoryAdmin,)
admin.site.register(Product, ProductAdmin,)
admin.site.register(Services, ServicesAdmin,)
# admin.site.register(Rates, RatesAdmin,)
admin.site.register(ProductStock, ProductStockAdmin,)
# admin.site.register(ProductResource,)