import django_filters
from django_filters.widgets import LinkWidget, BooleanWidget
from shop.models import Category, Product, Services
from shop import models

class ProductFilter(django_filters.FilterSet):
	CHOICES = [
			["name", "По Имени A-Z ▲"],
			["-name", "По Имени Z-A ▼"],
			["price", "По Ценк 0-1000 ▲"],
			["-price", "По Ценк 1000-0 ▼"],
		]
	CHOICES_available = [
		[True, 'Наличие ✔'],
		[False, 'Отсутствие ✖'],
	]
	l=[]
	l_vendor=[]
	l_type_product=[]
	l_category=[]

	for i in Product.objects.all():
		l_vendor.append((getattr(i, "vendor"), getattr(i, "vendor")))
		l_type_product.append((getattr(i, "type_product"), getattr(i, "type_product")))

		if ('', '') in l_vendor:
			l_vendor.remove(('', ''))

		if ('', '') in l_type_product:
			l_type_product.remove(('', ''))

	for i in Category.objects.all():
		if i.product.count():
			l_category.append((i.id, i.name))
			if ('', '') in l:
				l_category.remove(('', ''))

	l_type_product=set(l_type_product)
	l_vendor=set(l_vendor)
	l_category=set(l_category)

	price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Цена min - 0')
	price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Цена min - 0')
	available =django_filters.ChoiceFilter(choices=CHOICES_available, empty_label=None)
	ordering = django_filters.OrderingFilter(choices=CHOICES,empty_label=None)
	category=django_filters.ChoiceFilter(choices=sorted(l_category, key=lambda tup: tup[1]), empty_label='Категория')
	vendor=django_filters.ChoiceFilter(choices=sorted(l_vendor, key=lambda tup: tup[1]), empty_label='Производитель')
	type_product=django_filters.ChoiceFilter(choices=sorted(l_type_product, key=lambda tup: tup[1]), empty_label='Тип Товара')
	color_fild = django_filters.ChoiceFilter(field_name='color_fild', choices=models.COLOR_CHOICES, empty_label='BW/Color')
	format_fild = django_filters.ChoiceFilter(choices=models.FORMAT_CHOICES, empty_label='Формат A0-A10')

	class Meta:
		model = Product
		fields = [
			'price__gt',
			'price__lt',
			'available',
			'ordering',
			'category',
			'vendor',
			'type_product',
			'format_fild',
			'color_fild']


class ServiceFilter(django_filters.FilterSet):
	l_type_service=[]
	l_vendor=[]
	for i in Services.objects.all():
		l_type_service.append((getattr(i, "type_service"), getattr(i, "type_service")))
		l_vendor.append((getattr(i, "vendor"), getattr(i, "vendor")))

		if ('', '') in l_type_service:
			l_type_service.remove(('', ''))
		if ('', '') in l_vendor:
			l_vendor.remove(('', ''))

	l_type_service=set(l_type_service)
	l_vendor=set(l_vendor)

	CHOICES_CATEGORY_SERVICE = [
		['123','Авторизованный сервисный центр Ricoh'],
		['124','Авторизованный сервисный центр Konica Minolta'],
		['126','Ремонт Принтеров и МФУ'],
		['146','Заправка и ремонт картриджей'],
		['125','Ремонт компьютерной техники'],
	]

	price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Цена min - 0')
	price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Цена min - 0')
	type_service=django_filters.ChoiceFilter(choices=sorted(l_type_service, key=lambda tup: tup[1]), empty_label='Тип Сервиса')
	vendor=django_filters.ChoiceFilter(choices=sorted(l_vendor, key=lambda tup: tup[1]), empty_label='Производитель')
	category=django_filters.ChoiceFilter(choices=CHOICES_CATEGORY_SERVICE, empty_label='Категория')



# CHOICES_image =[
#         ["image", "▲"],
#         ["-image", "▼"]
# ]

# CHOICES_PRICE =[
#         ["price", "▲"],
#         ["-price", "▼"]
# ]

# CHOICES_available =[
#         ["available", "▲"],
#         ["-available", "▼"]
# ]

# CHOICES_NAME =[
#         ["name", "▲"],
#         ["-name", "▼"]
# ]

# CHOICES_VEND =[
#         ["vendor", "▲"],
#         ["-vendor", "▼"]
# ]
	# ordering_image = django_filters.OrderingFilter(
	# 	choices=CHOICES_image,
	# 	empty_label=None,
	# 	widget=LinkWidget)
	# ordering_price = django_filters.OrderingFilter(
	# 	choices=CHOICES_PRICE,
	# 	empty_label=None,
	# 	widget=LinkWidget)
	# ordering_available = django_filters.OrderingFilter(
	# 	choices=CHOICES_available,
	# 	empty_label=None,
	# 	widget=LinkWidget)
	# ordering_name = django_filters.OrderingFilter(
	# 	choices=CHOICES_NAME,
	# 	empty_label=None,
	# 	widget=LinkWidget)
	# ordering_vend = django_filters.OrderingFilter(
	# 	choices=CHOICES_VEND,
	# 	empty_label=None,
	# 	widget=LinkWidget)
