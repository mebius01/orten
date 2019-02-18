from shop.models import Category


def category(request):
	return {"category_all": Category.objects.all()}

# .objects.select_related('name').prefetch_related('slug').prefetch_related('parent').defer('description', 'image')