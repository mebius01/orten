from __future__ import unicode_literals
from django.shortcuts import render
from shop.models import Category, Services, Product, Polygraphy #, ProductStock

def product_update(request):
	products = Product.objects.all().order_by('-action', '-image')[:12]
	# some code
	ctx = {'products': products}
	return render(request, 'product_update.html', ctx)