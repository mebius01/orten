from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddProductForm
from taggit.models import Tag
# Create your views here.

def home(request):
	return render(request, 'shop/home.html')

def category(request):
	list_category = Category.objects.all()
	return render(request, 'shop/list_category.html', {'list_category': list_category})

def show_category(request,hierarchy=None,tag_id=None):
	category_slug = hierarchy.split('/')

	parent = None
	root = Category.objects.all()
	tag = None
	
	if tag_id:
		tag = get_object_or_404(Tag, slug=tag_id)
		product_list_all = porduct_list_all.filter(tags__in=[tag])

	for slug in category_slug[:-1]:
		parent = root.get(parent=parent, slug = slug)
	try:
		instance = Category.objects.get(parent=parent, slug=category_slug[-1])
	except:
		cart_product_form = CartAddProductForm()
		instance = get_object_or_404(Product, slug = category_slug[-1])
		category = Category.objects.get(product=instance)
		return render(request, "shop/product_detail.html", {'instance':instance, 'category':category, 'tag':tag, 'cart_product_form': cart_product_form})
	else:
		category = Category.objects.get(slug=category_slug[-1])
		products = Product.objects.filter(category=category)
		return render(request, 'shop/categories.html', {'category':category, 'products': products})


def product_list(request, tag_id=None):
	products = Product.objects.all()
	cart_product_form = CartAddProductForm()
	if tag_id:
		tag = get_object_or_404(Tag, id=tag_id)
		products = products.filter(tags__in=[tag])

	return render(request, 'shop/list.html', {'products': products, 'cart_product_form': cart_product_form})


def product_detail(request, slug):
	cart_product_form = CartAddProductForm()
	product = get_object_or_404(Product, slug=slug)
	category = Category.objects.get(product=product)
	return render(request, 'shop/product_detail.html', {'product': product, 'cart_product_form': cart_product_form, 'category':category,})