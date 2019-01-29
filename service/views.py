# from django.shortcuts import render

# # Create your views here.

# def category_servise(request, hierarchy=None):
# 		category_slug = hierarchy.split('/')

# 	parent = None
# 	category_all = Category.objects.all()

# 	# Форма количиства и корзины
# 	cart_product_form = CartAddProductForm()

# 	for slug in category_slug[:-1]:
# 		parent = category_all.get(parent=parent, slug = slug)
# 	try:
# 		instance = Category.objects.get(parent=parent, slug=category_slug[-1])
# 		print('AAAAAAA', instance)
# 	except:
# 		instance = get_object_or_404(Product, slug = category_slug[-1])
# 		category = Category.objects.get(product=instance)
# 		print('BBBBBBB', instance)
# 		return render( request, "shop/product_detail.html", {'instance':instance, 'category':category, 'cart_product_form': cart_product_form})
# 	else:
# 		category = Category.objects.get(slug=category_slug[-1])
# 		products = Product.objects.filter(category=category)
# 		print('CCCCC', category)
# 		return render(request, 'shop/categories.html', {'instance':instance, 'category':category, 'products': products, 'category_all':category_all, 'cart_product_form': cart_product_form})


from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from service.models import CategoryService, Services
# Create your views here.

def list_category(request, hierarchy=None):
	category_slug = hierarchy.split('/')

	parent = None
	category_all = CategoryService.objects.all()

	for slug in category_slug[:-1]:
		parent = category_all.get(parent=parent, slug = slug)
	try:
		instance = CategoryService.objects.get(parent=parent, slug=category_slug[-1])
	except:
		instance = get_object_or_404(Service, slug = category_slug[-1])
		category = CategoryService.get(service=instance)
		return render( request, "service/service_detail.html", {'instance':instance, 'category':category})
	else:
		category = CategoryService.objects.get(slug=category_slug[-1])
		services = Services.objects.filter(category=category)
		return render(request, 'service/list_category.html', {'instance':instance, 'category':category, 'services': services, 'category_all':category_all})


def category(request):
	category_all = CategoryService.objects.all()
	return render(request, 'service/category.html', {'category_all': category_all})