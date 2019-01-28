from django.contrib import admin
from .models import Category_Services, Services
from mptt.admin import MPTTModelAdmin
# Register your models here.

class Category_ServicesAdmin(MPTTModelAdmin):
	list_display = ['name', 'id', 'slug']
	prepopulated_fields = {'slug': ('name',)}
	mptt_level_indent = 30

class ServicesAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price']
	list_filter = ['name', 'price']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Services, ServicesAdmin,)
admin.site.register(Category_Services, Category_ServicesAdmin,)