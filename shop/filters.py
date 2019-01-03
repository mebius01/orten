import django_filters
from shop.models import Category, Product

class ProductFilter(django_filters.FilterSet):
	# vendor=django_filters.AllValuesFilter(widget=django_filters.widgets.LinkWidget)
	# price_purchase=django_filters.AllValuesFilter(widget=django_filters.widgets.RangeWidget)
	l=[]
	for i in Product.objects.all():
		l.append((i.vendor, i.vendor))
	vendor=django_filters.ChoiceFilter(choices=set(l))
	class Meta:
		model = Product
		fields = ['vendor']

# class ProductFilter(django_filters.FilterSet):
# 	# fields = django_filters.ModelChoiceFilter(field_name='vendor', lookup_expr='isnull', null_label='Uncategorized', queryset=Category.objects.all(),
# 	# )
# 	vendor = django_filters.ModelChoiceFilter(
#         lookup_expr='isnull',
#         to_field_name="vendor",
#         queryset=Product.objects.values_list("vendor", flat=True),
#     )

