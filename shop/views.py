from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category, Services, Product, Polygraphy #, ProductStock
from cart.forms import CartAddProductForm
from .filters import ProductFilter # ОСОБОЕ ВНИМЕНИЕ!!! При python manage.py makemigrations && python manage.py migrate КОМЕНТИРОВАТЬ ЭТУ СТРОКУ
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from watson import search as watson
from django.views.decorators.cache import cache_page
from django.db.models import Q
from .forms import FilterForm


def handler404(request):
	return render(request, '404.html', status=404)
def handler500(request):
	return render(request, '500.html', status=500)

def robots(request):
	return render_to_response('robots.txt', mimetype="text/plain")

def delivery_payment(request):
	return render(request, 'delivery_payment.html')

def contact(request):
	return render(request, 'contact.html')

def about(request):
	return render(request, 'about.html')

# @cache_page(60 * 15)
def category(request):
	return render(request, 'shop/category.html')

def home(request):
	product_stok = Product.objects.filter(action=True)
	products = Product.objects.all().order_by('-action')[:12]
	cart_product_form = CartAddProductForm()
	return render(request, 'shop/home.html', {'cart_product_form':cart_product_form, 'products':products, 'product_stok':product_stok})

# @cache_page(60 * 15)
def list_category(request, hierarchy=None):
	# Раззделяет строку УРЛа на список [категория, подкатегория, подкатегорияПодкатегории, итд]
	category_slug = hierarchy.split('/')
	parent = None
	category_all = Category.objects.all() # передать в контестный процессор
	for slug in category_slug[:-1]:
		parent = category_all.get(parent=parent, slug = slug)
	instance = Category.objects.get(parent=parent, slug=category_slug[-1])
	products = Product.objects.filter(category=instance)
	services = Services.objects.filter(category=instance)
	return render(request, 'shop/list_category.html', {'instance':instance, 'category':category, 'services':services, 'products': products})

def product_list(request):
	search = request.GET.get('search', '')
	category = request.GET.get('category', '')
	form = FilterForm()
	if search:
		product_list_all = watson.filter(Product, search, ranking=True)
	
	elif category:
		product_list_all = Product.objects.filter(category=category)
	
	else:
		product_list_all = Product.objects.all().order_by('-action')
	
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
	if len(category)>1:
		instance = Category.objects.get(id=category)
	else:
		instance = Category.objects.all()
	return render(request, 'shop/list_product.html', {'form': form, 'instance': instance, 'paginator':paginator, 'filter': products_filter, 'products': products, 'cart_product_form': cart_product_form})

def product_detail(request, slug):
	instance = get_object_or_404(Product, slug=slug)
	cart_product_form = CartAddProductForm()
	return render( request, "shop/product_detail.html", {'instance':instance, 'cart_product_form': cart_product_form})

def service_detail(request, slug):
	instance = get_object_or_404(Services, slug=slug)
	cart_product_form = CartAddProductForm()
	return render( request, "shop/service_detail.html", {'instance':instance, 'cart_product_form': cart_product_form})

def polygraphy_detail(request, flatpage_id):
	instance = get_object_or_404(Polygraphy, flatpage_id=flatpage_id)
	return render( request, "shop/polygraphy_detail.html", {'instance':instance})

def polygraphy(request):
	return render( request, "shop/polygraphy.html")