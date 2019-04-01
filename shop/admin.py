from django.contrib import admin
from .models import Category, Product, Services, Polygraphy # ProductStock,
from mptt.admin import MPTTModelAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage


class CategoryAdmin(MPTTModelAdmin):
	list_display = ['name', 'id', 'slug']
	prepopulated_fields = {'slug': ('name',)}
	mptt_level_indent = 30

class ProductResource(resources.ModelResource):
	class Meta:
		model = Product
		fields = ('id', 'category','name', 'provider', 'vendor', 'vendor_code', 'specifications', 'type_product', 'slug','price','stock','available')

class ProductAdmin(ImportExportModelAdmin):
	search_fields = ['name', 'vendor_code',]
	list_display = ['name', 'id', 'action', 'color_fild', 'format_fild', 'price', 'stock', 'available', 'updated']
	list_filter = ['provider', 'type_product','category', 'action', 'created', 'updated', 'vendor', 'available']
	list_editable = ['price', 'stock', 'available', 'action', 'color_fild', 'format_fild']
	prepopulated_fields = {'slug': ('name','vendor_code')}
	resource_class = ProductResource

class ServicesAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price']
	list_filter = ['name', 'price']
	prepopulated_fields = {'slug': ('name',)}

# class PolygraphyAdmin(admin.ModelAdmin):
# 	list_display = ['name', 'slug',]
# 	list_filter = ['name', ]
# 	prepopulated_fields = {'slug': ('name',)}

class NewFlatpageInline(admin.StackedInline):
	model = Polygraphy
	verbose_name = "Содержание"

class FlatPageNewAdmin(FlatPageAdmin):
	inlines = [NewFlatpageInline]
	fieldsets = ((None, {'fields': ('url', 'title', 'sites', 'content',)}),(('Advanced options'), {'fields': ('template_name',),}),)
	list_display = ('url', 'title',)
	list_filter = ('sites', 'registration_required')
	search_fields = ('url', 'title')

# class ProductStockAdmin(admin.ModelAdmin):
# 	list_display = ['id', 'stock_start', 'stock_end', 'product', 'slug', 'description',]
# 	list_filter = ['stock_start', 'stock_end', 'product',]
# 	prepopulated_fields = {'slug': ('product',)}

admin.site.register(Category, CategoryAdmin,)
admin.site.register(Product, ProductAdmin,)
admin.site.register(Services, ServicesAdmin,)
# admin.site.register(ProductStock, ProductStockAdmin,)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageNewAdmin)