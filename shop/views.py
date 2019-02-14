from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category, Services, Product, ProductStock
from cart.forms import CartAddProductForm
from .filters import ProductFilter # ОСОБОЕ ВНИМЕНИЕ!!! При python manage.py makemigrations && python manage.py migrate КОМЕНТИРОВАТЬ ЭТУ СТРОКУ
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from watson import search as watson

def delivery_payment(request):
	return render(request, 'delivery_payment.html')

def contact(request):
	return render(request, 'contact.html')

def category(request):
	return render(request, 'shop/category.html')

def home(request):
	product_stok = ProductStock.objects.all()
	products = Product.objects.all().order_by()[:9]
	cart_product_form = CartAddProductForm()
	return render(request, 'shop/home.html', {'cart_product_form':cart_product_form, 'products':products, 'product_stok':product_stok})

def list_category(request, hierarchy=None):
	# Раззделяет строку УРЛа на список [категория, подкатегория, подкатегорияПодкатегории, итд]
	category_slug = hierarchy.split('/')
	parent = None

	for slug in category_slug[:-1]:
		parent = category_all.get(parent=parent, slug = slug)
	instance = Category.objects.get(parent=parent, slug=category_slug[-1])
	products = Product.objects.filter(category=instance)
	services = Services.objects.filter(category=instance)
	return render(request, 'shop/list_category.html', {'instance':instance, 'category':category, 'services':services, 'products': products})

def product_list(request):
	search = request.GET.get('search', '')
	if search:
		product_list_all = watson.filter(Product, search, ranking=True)
	else:
		product_list_all = Product.objects.all().order_by('-updated')
	products_filter = ProductFilter(request.GET, queryset=product_list_all)
	page = request.GET.get('page', 1)
	paginator = Paginator(products_filter.qs, 48)
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		# Если страница не является целым числом, показать первую страницу.
		products = paginator.page(1)
	except EmptyPage:
		# Если страница выходит за пределы допустимого диапазона (например, 9999), казать последнюю страницу результатов
		products = paginator.page(paginator.num_pages)
	cart_product_form = CartAddProductForm()
	return render(request, 'shop/list_product.html', {'paginator':paginator, 'filter': products_filter, 'products': products, 'cart_product_form': cart_product_form})

def product_detail(request, slug):
	instance = get_object_or_404(Product, slug=slug)
	cart_product_form = CartAddProductForm()
	return render( request, "shop/product_detail.html", {'instance':instance, 'cart_product_form': cart_product_form})

def service_detail(request, slug):
	instance = get_object_or_404(Services, slug=slug)
	cart_product_form = CartAddProductForm()
	return render( request, "shop/service_detail.html", {'instance':instance, 'cart_product_form': cart_product_form})