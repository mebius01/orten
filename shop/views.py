from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product, ProductStock
from cart.forms import CartAddProductForm
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from shop.filters import ProductFilter

def home(request):
	product_stok = ProductStock.objects.all()
	category = Category.objects.all()
	products = Product.objects.all()
	cart_product_form = CartAddProductForm()
	return render(request, 'shop/home.html', {'cart_product_form':cart_product_form, 'products':products, 'product_stok':product_stok, 'category':category})

# тестовый шаблон
def _test(request):
	return render(request, 'base-test.html')

def category(request):
	category_all = Category.objects.all()
	return render(request, 'shop/list_category.html', {'category_all': category_all})

def show_category(request,hierarchy=None,tag_id=None):
	category_slug = hierarchy.split('/')

	parent = None
	root = Category.objects.all()
	tag = None
	cart_product_form = CartAddProductForm()
	if tag_id:
		tag = get_object_or_404(Tag, slug=tag_id)
		product_list_all = porduct_list_all.filter(tags__in=[tag])

	for slug in category_slug[:-1]:
		parent = root.get(parent=parent, slug = slug)
	try:
		instance = Category.objects.get(parent=parent, slug=category_slug[-1])
	except:
		instance = get_object_or_404(Product, slug = category_slug[-1])
		category = Category.objects.get(product=instance)
		return render(request, "shop/product_detail.html", {'instance':instance, 'category':category, 'tag':tag, 'cart_product_form': cart_product_form})
	else:
		category = Category.objects.get(slug=category_slug[-1])
		products = Product.objects.filter(category=category)
		category_all = Category.objects.all()
		return render(request, 'shop/categories.html', {'category':category, 'products': products, 'category_all':category_all, 'cart_product_form': cart_product_form})

def search(request):
	products = Product.objects.all()
	products_filter = ProductFilter(request.GET, queryset=products)
	return render(request, 'shop/list.html', {'filter': products_filter, 'products':products})

def product_list(request):
	products_filter = ProductFilter(request.GET, queryset=Product.objects.all())
	page = request.GET.get('page', 1)
	paginator = Paginator(products_filter.qs, 80)
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		# Если страница не является целым числом, показать первую страницу.
		products = paginator.page(1)
	except EmptyPage:
		# Если страница выходит за пределы допустимого диапазона (например, 9999), казать последнюю страницу результатов
		products = paginator.page(paginator.num_pages)

	cart_product_form = CartAddProductForm()
	return render(request, 'shop/list.html', {'filter': products_filter, 'products': products, 'cart_product_form': cart_product_form})



def product_detail(request, slug):
	cart_product_form = CartAddProductForm()
	product = get_object_or_404(Product, slug=slug)
	category = Category.objects.get(product=product)
	return render(request, 'shop/product_detail.html', {'product': product, 'cart_product_form': cart_product_form, 'category':category,})
