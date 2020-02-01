import django_filters
from django_filters.widgets import LinkWidget
from shop.models import Category, Product, Services
from shop import models

CHOICES_image =[
        ["image", "▲"],
        ["-image", "▼"]
]

CHOICES_PRICE =[
        ["price", "▲"],
        ["-price", "▼"]
]

CHOICES_available =[
        ["available", "▲"],
        ["-available", "▼"]
]

CHOICES_NAME =[
        ["name", "▲"],
        ["-name", "▼"]
]

CHOICES_VEND =[
        ["vendor", "▲"],
        ["-vendor", "▼"]
]

CHOICES = [
		["image", "По Картинке ▲"],
        ["-image", "По Картинке ▼"],
		["price", "По Цене ▲"],
        ["-price", "По Цене ▼"],
		["available", "По Наличию ▲"],
        ["-available", "По Наличию ▼"],
		["name", "По Имени ▲"],
        ["-name", "По Имени ▼"],
		["vendor", "По Бренду ▲"],
        ["-vendor", "по Бренду ▼"]

]

# CHOICES_VEND =[
#         ["vendor", "▲"],
#         ["-vendor", "▼"]
# ]

# CHOICES_VEND =[
#         ["vendor", "▲"],
#         ["-vendor", "▼"]
# ]

# vendor_code available


class ProductFilter(django_filters.FilterSet):
	price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='min')
	price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='max')

	ordering_image = django_filters.OrderingFilter(
		choices=CHOICES_image,
		empty_label=None,
		widget=LinkWidget)

	ordering_price = django_filters.OrderingFilter(
		choices=CHOICES_PRICE,
		empty_label=None,
		widget=LinkWidget)

	ordering_available = django_filters.OrderingFilter(
		choices=CHOICES_available,
		empty_label=None,
		widget=LinkWidget)	
	
	ordering_name = django_filters.OrderingFilter(
		choices=CHOICES_NAME,
		empty_label=None,
		widget=LinkWidget)
	
	ordering_vend = django_filters.OrderingFilter(
		choices=CHOICES_VEND,
		empty_label=None,
		widget=LinkWidget)	

	ordering = django_filters.OrderingFilter(
		choices=CHOICES,
		required=True,
		empty_label="All")

	l=[]
	for i in Product.objects.all():
		l.append((getattr(i, "vendor"), getattr(i, "vendor")))
		if ('', '') in l:
			l.remove(('', ''))
	l=set(l)
	vendor=django_filters.ChoiceFilter(choices=sorted(l, key=lambda tup: tup[1]), empty_label='Производитель')

	l=[]
	for i in Product.objects.all():
		l.append((getattr(i, "type_product"), getattr(i, "type_product")))
		if ('', '') in l:
			l.remove(('', ''))
	l=set(l)
	type_product=django_filters.ChoiceFilter(choices=sorted(l, key=lambda tup: tup[1]), empty_label='Тип Товара')

	l=[]
	for i in Category.objects.all():
		l.append((i.id, i.name))
		if ('', '') in l:
			l.remove(('', ''))
	l=set(l)
	category=django_filters.ChoiceFilter(choices=sorted(l, key=lambda tup: tup[1]), empty_label='Категория')
	color_fild = django_filters.ChoiceFilter(field_name='color_fild', choices=models.COLOR_CHOICES, empty_label='BW/Color')
	format_fild = django_filters.ChoiceFilter(choices=models.FORMAT_CHOICES, empty_label='Формат A0-A10')

	class Meta:
		model = Product
		fields = ['price__gt', 'price__lt', 'ordering_price', 'category', 'vendor', 'type_product', 'format_fild', 'color_fild']


class ServiceFilter(django_filters.FilterSet):

	price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='min')
	price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='max')

	l=[]
	for i in Services.objects.all():
		l.append((getattr(i, "type_service"), getattr(i, "type_service")))
		if ('', '') in l:
			l.remove(('', ''))
	l=set(l)
	type_service=django_filters.ChoiceFilter(choices=sorted(l, key=lambda tup: tup[1]), empty_label='Тип Сервиса')

	l=[]
	for i in Services.objects.all():
		l.append((getattr(i, "vendor"), getattr(i, "vendor")))
		if ('', '') in l:
			l.remove(('', ''))
	l=set(l)
	vendor=django_filters.ChoiceFilter(choices=sorted(l, key=lambda tup: tup[1]), empty_label='Производитель')

	l=[]
	for i in Category.objects.all():
		l.append((i.id, i.name))
		if ('', '') in l:
			l.remove(('', ''))
	l=set(l)
	category=django_filters.ChoiceFilter(choices=sorted(l, key=lambda tup: tup[1]), empty_label='Категория')





	# category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all().get_descendants(), conjoined=True, label="Фильтр по категориям")

	# vendor1=django_filters.AllValuesFilter(widget=django_filters.widgets.LinkWidget)
	# price=django_filters.AllValuesFilter(widget=django_filters.widgets.RangeWidget)
	 # = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)
# class ProductFilter(django_filters.FilterSet):
# 	# fields = django_filters.ModelChoiceFilter(field_name='vendor', lookup_expr='isnull', null_label='Uncategorized', queryset=Category.objects.all(),
# 	# )
# 	vendor = django_filters.ModelChoiceFilter(
#         lookup_expr='isnull',
#         to_field_name="vendor",
#         queryset=Product.objects.values_list("vendor", flat=True),
#     )

	# l=[]
	# for i in Product.objects.all():
	# 	l.append((i.format_fild, i.format_fild))
	# 	if ('', '') in l:
	# 		l.remove(('', ''))
	# format_fild = django_filters.ChoiceFilter(choices=set(l), empty_label='Формат A0-A10')
	# format_fild = django_filters.ModelChoiceFilter(label="Фильтр по Формату")

	# l=[]
	# for i in Product.objects.all():
	# 	l.append((i.color_fild, i.color_fild))
	# 	if ('', '') in l:
	# 		l.remove(('', ''))
	# color_fild = django_filters.ChoiceFilter(choices=set(l), empty_label='BW/Color')

	# l=[]
	# for i in Product.objects.all():
	# 	l.append((i.category_id, i.category))
	# 	if ('', '') in l:
	# 		l.remove(('', ''))