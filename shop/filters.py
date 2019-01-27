import django_filters
from shop.models import Category, Product
from django.contrib.postgres.search import SearchVector

class ProductFilter(django_filters.FilterSet):
	# vendor1=django_filters.AllValuesFilter(widget=django_filters.widgets.LinkWidget)
	# price=django_filters.AllValuesFilter(widget=django_filters.widgets.RangeWidget)
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

	search=Product.objects.annotate(search=SearchVector('vendor_code', 'name', 'description'),).filter(search='')


	class Meta:
		model = Product
		fields = ['vendor', 'type_product', 'price__gt', 'price__lt', 'category']# , 'vendor_code']

# class ProductFilter(django_filters.FilterSet):
# 	# fields = django_filters.ModelChoiceFilter(field_name='vendor', lookup_expr='isnull', null_label='Uncategorized', queryset=Category.objects.all(),
# 	# )
# 	vendor = django_filters.ModelChoiceFilter(
#         lookup_expr='isnull',
#         to_field_name="vendor",
#         queryset=Product.objects.values_list("vendor", flat=True),
#     )

