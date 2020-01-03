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
from django_filters.views import FilterView

def handler404(request, exception):
	return render(request, '404.html', status=404)
def handler500(request, exception):
	return render(request, '500.html', status=500)
def robots(request):
	return render('robots.txt', mimetype="text/plain")

class Home(ListView, FormView):
	model = Product
	template_name = 'shop/home.html'
	form_class = CartAddProductForm
	queryset = Product.objects.all().order_by('-action', '-image')[:12]

class ProductDetail(DetailView, FormView):
	model = Product
	template_name = 'shop/product_detail.html'
	form_class = CartAddProductForm

class ListCategory(ListView):
	model = Product
	template_name = 'shop/list_category.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		leaf = self.request.get_full_path().split('/')[-2]
		instance = Category.objects.get(slug=leaf)
		context['instance'] = instance
		context['products'] = Product.objects.filter(category=instance.id)
		context['services'] = Services.objects.filter(category=instance.id)
		return context

# class FilterListView(ListView):
# 	filterset_class = None
# 	def get_queryset(self):
# 		queryset = super().get_queryset()
# 		self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
# 		return self.filterset.qs.distinct()
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['filterset'] = self.filterset
# 		return context

class FilteredListView(ListView):
    filterset_class = None
    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context

class ProductList(FormView, ListView):
	model = Product
	template_name = 'test_list_product.html'
	form_class = CartAddProductForm
	paginate_by = 24
	filterset_class = ProductFilter

	def get_queryset(self):
		qs = Product.objects.all()
		try:
			search = self.request.GET['search']
			qs = qs.annotate(
				search=(
					SearchVector('name')+
					SearchVector('description')+
					SearchVector('vendor_code')+
					SearchVector('specifications')
				),
			).filter(search=search)
			queryset = qs.order_by('-action', '-image')
		except KeyError:
			category = self.request.GET.get('category')
			if category:
				queryset = qs.filter(category=category).order_by('-action', '-image')
			else:
				queryset =  qs.order_by('-action', '-image')
		self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
		return self.filterset.qs.distinct()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		category = self.request.GET.get('category')
		if category:
			context['instance'] = Category.objects.get(id=category)
		else:
			context['instance'] = Category.objects.all()
		context['filterset'] = self.filterset
		return context

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
