from shop.models import Category

def category(request):
	return {"category_all": Category.objects.all()}