from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
# Create your views here.

def category(request):
	list_category = Category.objects.all()
	return render(request, 'shop/list_category.html', {'list_category': list_category})

def show_category(request,hierarchy=None, tag_slug=None):
	category_slug = hierarchy.split('/')

	parent = None
	root = Category.objects.all()
	tag = None
	
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		product_list_all = porduct_list_all.filter(tags__in=[tag])
	print(tag)
	for slug in category_slug[:-1]:
		parent = root.get(parent=parent, slug = slug)
	try:
		instance = Category.objects.get(parent=parent, slug=category_slug[-1])
	except:
		category = Category.objects.filter(slug=category_slug[-2])
		instance = get_object_or_404(Product, slug = category_slug[-1])
		return render(request, "shop/postDetail.html", {'instance':instance, 'category':category, 'tag':tag})
	else:
		category = Category.objects.filter(slug=category_slug[-2])
		return render(request, 'shop/categories.html', {'instance':instance, 'category':category, 'tag':tag})
		print(tag)


def product_list(request):
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	return render(request, 'shop/product/list.html', {'categories': categories, 'products': products})


# def product_detail(request, slug):
# 	print('qq')
# 	product = get_object_or_404(Product, slug=slug, available=True)
# 	return render(request, 'shop/product_card.html', {'product': product})