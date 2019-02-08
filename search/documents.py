from django_elasticsearch_dsl import DocType, Index
from shop.models import Product

product = Index('product')

@product.doc_type
class ProductDocument(DocType):
	class Meta:
		model = Product
		fields = ['name','id','vendor_code','description',]