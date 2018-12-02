from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product

from taggit.models import Tag
# Create your views here.

def category(request):
	list_category = Category.objects.all()
	return render(request, 'shop/list_category.html', {'list_category': list_category})

def show_category(request,hierarchy=None, tag_id=None):
	category_slug = hierarchy.split('/')

	parent = None
	root = Category.objects.all()
	tag = None
	
	if tag_id:
		tag = get_object_or_404(Tag, slug=tag_id)
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
		category = Category.objects.filter(slug=category_slug[-1])
		return render(request, 'shop/categories.html', {'instance':instance, 'category':category, 'tag':tag})
		print(tag)

# def product_detail(request, product_slug):
# 	instance = Product.objects.get(slug=product_slug)
# 	category = Category.objects.all()
# 	return render(request, 'shop/postDetail.html', {'instance':instance, 'category':category})

def product_list(request, tag_id=None):
	products = Product.objects.all()
	if tag_id:
		tag = get_object_or_404(Tag, id=tag_id)
		products = products.filter(tags__in=[tag])
	return render(request, 'shop/product/list.html', {'products': products})


# def product_detail(request, slug):
# 	print('qq')
# 	product = get_object_or_404(Product, slug=slug, available=True)
# 	return render(request, 'shop/product_card.html', {'product': product})