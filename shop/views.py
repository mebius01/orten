from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
# Create your views here.

def category(request):
# 	slugs = full_slug.split('/')
# 	page_slug = slugs[-1]
# 	page = get_object_or_404(Category ,slug=page_slug)
# 	if not page.get_absolute_url().strip('/') == full_slug:
# 		raise Http404
	return render(request, 'shop/list_category.html', {'category': Category.objects.all()})

def show_category(request,hierarchy= None):
	category_slug = hierarchy.split('/')
	parent = None
	root = Category.objects.all()

	for slug in category_slug[:-1]:
		parent = root.get(parent=parent, slug = slug)

	try:
		instance = Category.objects.get(parent=parent, slug=category_slug[-1])
	except:
		instance = get_object_or_404(Product, slug = category_slug[-1])
		return render(request, "shop/postDetail.html", {'instance':instance})
	else:
		return render(request, 'shop/categories.html', {'instance':instance, 'category': Category.objects.all()})


def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	return render(request, 'shop/product_card.html',  {'product': product})