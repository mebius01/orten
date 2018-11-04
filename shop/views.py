from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.
def base(request):
	return render(request, 'base.html')

def category_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request, 'shop/category_list.html', {'category': category, 'categories': categories, 'products': products})


def product_card(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	return render(request, 'shop/product_card.html',  {'product': product})