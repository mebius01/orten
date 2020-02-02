from django.contrib import admin
from .models import Rates, Category, Product, Services, Polygraphy # ProductStock,
from mptt.admin import MPTTModelAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage

class RatesAdmin(admin.ModelAdmin):
	list_display = ['created', 'usd', 'eur']

class CategoryAdmin(MPTTModelAdmin):
	list_display = ['name', 'id', 'slug']
	prepopulated_fields = {'slug': ('name',)}
	mptt_level_indent = 30

class ProductResource(resources.ModelResource):
	class Meta:
		model = Product
		fields = ('id', 'category','name', 'provider', 'vendor', 'vendor_code', 'type_product', 'slug','price', 'available')

class ProductAdmin(ImportExportModelAdmin):
	search_fields = ['name', 'vendor_code',]
	list_display = ['name', 'available', 'price', 'action', 'start_action', 'end_action', 'color_fild', 'format_fild']
	list_filter = ['action', 'created', 'updated', 'available', 'provider', 'type_product','category', 'vendor']
	list_editable = ['price', 'available', 'action', 'start_action', 'end_action', 'color_fild', 'format_fild']
	prepopulated_fields = {'slug': ('name','vendor_code')}
	resource_class = ProductResource

class ServicesResource(resources.ModelResource):
	class Meta:
		model = Services
		fields = ('id', 'category','name', 'slug', 'vendor', 'vendor_code', 'vendor_model', 'description', 'price')

class ServicesAdmin(ImportExportModelAdmin):
	search_fields = ['name','vendor_code','vendor_model']
	list_display = ['name','vendor','vendor_code','price','updated','created']
	list_filter = ['vendor', 'type_service', 'price', 'name']
	prepopulated_fields = {'slug': ('name', 'vendor_code')}
	resource_class = ServicesResource

class NewFlatpageInline(admin.StackedInline):
	model = Polygraphy
	verbose_name = "Содержание"

class FlatPageNewAdmin(FlatPageAdmin):
	inlines = [NewFlatpageInline]
	fieldsets = ((None, {'fields': ('url', 'title', 'sites', 'content',)}),(('Advanced options'), {'fields': ('template_name',),}),)
	list_display = ('url', 'title',)
	list_filter = ('sites', 'registration_required')
	search_fields = ('url', 'title')

admin.site.register(Rates, RatesAdmin)
admin.site.register(Category, CategoryAdmin,)
admin.site.register(Product, ProductAdmin,)
admin.site.register(Services, ServicesAdmin,)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageNewAdmin)