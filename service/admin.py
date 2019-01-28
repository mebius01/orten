from django.contrib import admin
from .models import CategoryService, Services
from mptt.admin import MPTTModelAdmin
# Register your models here.

class CategoryServiceAdmin(MPTTModelAdmin):
	list_display = ['name', 'id', 'slug']
	prepopulated_fields = {'slug': ('name',)}
	mptt_level_indent = 30

class ServicesAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price']
	list_filter = ['name', 'price']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Services, ServicesAdmin,)
admin.site.register(CategoryService, CategoryServiceAdmin,)