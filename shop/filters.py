import django_filters
from django_filters.widgets import LinkWidget
from shop.models import Category, Product

class ProductFilter(django_filters.FilterSet):
	# vendor1=django_filters.AllValuesFilter(widget=django_filters.widgets.LinkWidget)
	# price=django_filters.AllValuesFilter(widget=django_filters.widgets.RangeWidget)
	 # = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)
	price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='min')
	price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='max')

	l=[]
	for i in Product.objects.all():
		l.append((i.vendor, i.vendor))
	vendor=django_filters.ChoiceFilter(choices=set(l), empty_label='Вендор')

	l=[]
	for i in Product.objects.all():
		l.append((i.type_product, i.type_product))
	type_product=django_filters.ChoiceFilter(choices=set(l), empty_label='Тип Товара')

	l=[]
	for i in Product.objects.all():
		l.append((i.format_fild, i.format_fild))
	format_fild = django_filters.ChoiceFilter(choices=set(l), empty_label='Формат A0-A10')

	color_fild = django_filters.AllValuesFilter(widget=LinkWidget())

	class Meta:
		model = Product
		fields = ['vendor', 'type_product', 'price__gt', 'price__lt', 'category', 'format_fild', 'color_fild',]# , 'vendor_code']

# class ProductFilter(django_filters.FilterSet):
# 	# fields = django_filters.ModelChoiceFilter(field_name='vendor', lookup_expr='isnull', null_label='Uncategorized', queryset=Category.objects.all(),
# 	# )
# 	vendor = django_filters.ModelChoiceFilter(
#         lookup_expr='isnull',
#         to_field_name="vendor",
#         queryset=Product.objects.values_list("vendor", flat=True),
#     )

