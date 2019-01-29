from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product, ProductStock
from cart.forms import CartAddProductForm
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from shop.filters import ProductFilter
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import TrigramSimilarity
from django.http import Http404


def home(request):
	product_stok = ProductStock.objects.all()
	category_all = Category.objects.all()
	products = Product.objects.all().order_by()[:9]
	cart_product_form = CartAddProductForm()
	return render(request, 'shop/home.html', {'cart_product_form':cart_product_form, 'products':products, 'product_stok':product_stok, 'category_all':category_all})



# тестовый шаблон
def _test(request):
	return render(request, 'base-test.html')

def category(request):
	category_all = Category.objects.all()
	return render(request, 'shop/category.html', {'category_all': category_all})

def list_category(request, hierarchy=None):
	# Раззделяет строку УРЛа на список [категория, подкатегория, подкатегорияПодкатегории, итд]
	category_slug = hierarchy.split('/')

	parent = None
	category_all = Category.objects.all()

	# Форма количиства и корзины
	cart_product_form = CartAddProductForm()

	for slug in category_slug[:-1]:
		parent = category_all.get(parent=parent, slug = slug)
	try:
		instance = Category.objects.get(parent=parent, slug=category_slug[-1])
		print('AAAAAAA', instance)
	except:
		instance = get_object_or_404(Product, slug = category_slug[-1])
		category = Category.objects.get(product=instance)
		print('BBBBBBB', instance)
		return render( request, "shop/product_detail.html", {'instance':instance, 'category':category, 'cart_product_form': cart_product_form})
	else:
		category = Category.objects.get(slug=category_slug[-1])
		products = Product.objects.filter(category=category)
		print('CCCCC', category)
		return render(request, 'shop/list_category.html', {'instance':instance, 'category':category, 'products': products, 'category_all':category_all, 'cart_product_form': cart_product_form})




def search(request):
	products = Product.objects.all()
	products_filter = ProductFilter(request.GET, queryset=products)
	return render(request, 'shop/list.html', {'filter': products_filter, 'products':products})

def product_list(request):
	search = request.GET.get('search', '')
	if search:
		product_list_all = Product.objects.annotate(search=SearchVector('vendor_code', 'name', 'description'),).filter(search=search)
	else:
		product_list_all = Product.objects.all().order_by('-updated')
	products_filter = ProductFilter(request.GET, queryset=product_list_all)
	page = request.GET.get('page', 1)
	paginator = Paginator(products_filter.qs, 2)
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		# Если страница не является целым числом, показать первую страницу.
		products = paginator.page(1)
	except EmptyPage:
		# Если страница выходит за пределы допустимого диапазона (например, 9999), казать последнюю страницу результатов
		products = paginator.page(paginator.num_pages)

	cart_product_form = CartAddProductForm()
	return render(request, 'shop/list.html', {'paginator':paginator, 'filter': products_filter, 'products': products, 'cart_product_form': cart_product_form})



def product_detail(request, slug):
	cart_product_form = CartAddProductForm()
	product = get_object_or_404(Product, slug=slug)
	category = Category.objects.get(product=product)
	return render(request, 'shop/product_detail.html', {'product': product, 'cart_product_form': cart_product_form, 'category':category,})
