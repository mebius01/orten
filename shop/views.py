from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category, Services, Product, Polygraphy #, ProductStock
from cart.forms import CartAddProductForm
from .filters import ProductFilter # ОСОБОЕ ВНИМЕНИЕ!!! При python manage.py makemigrations && python manage.py migrate КОМЕНТИРОВАТЬ ЭТУ СТРОКУ
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from watson import search as watson
from django.views.decorators.cache import cache_page
from django.db.models import Q
from django.core.cache import cache

from django.views.generic import TemplateView, ListView, DetailView, FormView

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

def handler404(request, exception):
	return render(request, '404.html', status=404)

def handler500(request, exception):
	return render(request, '500.html', status=500)

def robots(request):
	return render_to_response('robots.txt', mimetype="text/plain")

def search_console(request):
	return render(request, 'googledd11b6ee42c918f5.html')

class DeliveryPayment(TemplateView):
	template_name = 'delivery_payment.html'
	# return render(request, 'delivery_payment.html')

class Contact(TemplateView):
	template_name = 'contact.html'

class About(TemplateView):
	template_name = 'about.html'

# @cache_page(60 * 15)
class Categories(TemplateView):
	template_name = 'shop/category.html'

class Home(ListView, FormView):
	model = Product
	template_name = 'shop/home.html'
	form_class = CartAddProductForm
	queryset = Product.objects.all().order_by('-action', '-image')[:12]
	# def get_context_data(self, **kwargs):
	#     context = super().get_context_data(**kwargs)
	#     context['category_all'] = Category.objects.all()
	#     return context

	# product_stok = Product.objects.filter(action=True)
	# products = Product.objects.all().order_by('-action', '-image')[:12] #'-available'
	# cart_product_form = CartAddProductForm()
	# return render(request, 'shop/home.html', {'cart_product_form':cart_product_form, 'products':products, 'product_stok':product_stok})

class ProductDetail(DetailView, FormView):
	model = Product
	template_name = 'shop/product_detail.html'
	form_class = CartAddProductForm

	# instance = get_object_or_404(Product, slug=slug)
	# cart_product_form = CartAddProductForm()
	# return render( request, "shop/product_detail.html", {'instance':instance, 'cart_product_form': cart_product_form})

class ServiceDetail(DetailView):
	model = Services
	template_name = 'shop/service_detail.html'

	# instance = get_object_or_404(Services, slug=slug)
	# cart_product_form = CartAddProductForm()
	# return render( request, "shop/service_detail.html", {'instance':instance, 'cart_product_form': cart_product_form})

class PolygraphyDetail(DetailView):
	model = Polygraphy
	template_name = 'shop/polygraphy_detail.html'

	# instance = get_object_or_404(Polygraphy, flatpage_id=flatpage_id)
	# return render( request, "shop/polygraphy_detail.html", {'instance':instance})

class Polygraphy(TemplateView):
	template_name = "shop/polygraphy.html"

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
	return render(request, 'shop/list_category.html', {'instance':instance, 'services':services, 'products': products})

class FilterListView(ListView):
	filterset_class = None
	def get_queryset(self):
		queryset = super().get_queryset()
		self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
		return self.filterset.qs.distinct()
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		category = self.request.GET.get('category')
		search_string = self.request.GET.get('search')
		if search_string:
			queryset = watson.filter(Product, search_string, ranking=True)
		elif category:
			if len(category)>1:
				instance = Category.objects.get(id=category)
				context['instance'] = instance
			else:
				instance = Category.objects.all()
				context['instance'] = instance
		context['filter'] = self.filterset
		return context


# if search_string:
# 			try:
# 				queryset = queryset.annotate(
# 					search=(
# 						SearchVector('name')+
# 						SearchVector('description')+
# 						SearchVector('vendor_code')+
# 						SearchVector('specifications')
# 					),
# 				).filter(search=SearchQuery(search_string))
# 			except KeyError:
# 				return Product.objects.none()


class ProductList(FilterListView):
	model = Product
	template_name = 'test_list_product.html'
	form_class = CartAddProductForm
	queryset = Product.objects.all().order_by('-action', '-image')
	paginate_by = 24
	filterset_class = ProductFilter


def product_list(request):
	search = request.GET.get('search', '')
	category = request.GET.get('category', '')
	if search:
		product_list_all = watson.filter(Product, search, ranking=True)
	elif category:
		product_list_all = Product.objects.filter(category=category).order_by('-action', '-image')
	else:
		product_list_all = Product.objects.all().order_by('-action', '-image')
	products_filter = ProductFilter(request.GET, queryset=product_list_all)
	page = request.GET.get('page', 1)
	paginator = Paginator(products_filter.qs, 24)
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
	return render(request, 'shop/list_product.html', {'search': search, 'instance': instance, 'paginator':paginator, 'filter': products_filter, 'products': products, 'cart_product_form': cart_product_form})

def test(request):
	pass
