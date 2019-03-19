import django_filters
from django_filters.widgets import LinkWidget
from shop.models import Category, Product

class ProductFilter(django_filters.FilterSet):
	price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='min')
	price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='max')

	l=[]
	for i in Product.objects.all():
		l.append((i.vendor, i.vendor))
		if ('', '') in l:
			l.remove(('', ''))
	vendor=django_filters.ChoiceFilter(choices=set(l), empty_label='Производитель')

	l=[]
	for i in Product.objects.all():
		l.append((i.type_product, i.type_product))
		if ('', '') in l:
			l.remove(('', ''))
	type_product=django_filters.ChoiceFilter(choices=set(l), empty_label='Тип Товара')

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
	category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all().get_descendants(), conjoined=True, label="Фильтр по категориям")

	class Meta:
		model = Product
		fields = ['vendor', 'type_product', 'price__gt', 'price__lt', 'category', 'format_fild', 'color_fild']



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

