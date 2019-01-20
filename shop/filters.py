import django_filters
from shop.models import Category, Product

class ProductFilter(django_filters.FilterSet):
	# vendor1=django_filters.AllValuesFilter(widget=django_filters.widgets.LinkWidget)
	# price=django_filters.AllValuesFilter(widget=django_filters.widgets.RangeWidget)
	
	
	l=[]
	for i in Product.objects.all():
		l.append((i.vendor, i.vendor))
	vendor=django_filters.ChoiceFilter(choices=set(l))
	

	l=[]
	for i in Product.objects.all():
		l.append((i.type_product, i.type_product))
	type_product=django_filters.ChoiceFilter(choices=set(l), label='Type product')
	
	class Meta:
		model = Product
		fields = ['vendor', 'type_product']

# class ProductFilter(django_filters.FilterSet):
# 	# fields = django_filters.ModelChoiceFilter(field_name='vendor', lookup_expr='isnull', null_label='Uncategorized', queryset=Category.objects.all(),
# 	# )
# 	vendor = django_filters.ModelChoiceFilter(
#         lookup_expr='isnull',
#         to_field_name="vendor",
#         queryset=Product.objects.values_list("vendor", flat=True),
#     )

