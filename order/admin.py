from django.contrib import admin

# Register your models here.

from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_field = ['product']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'email', 'city', 'paid', 'created', 'updated']
	list_filter = ['paid', 'created', 'updated']
	inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)


