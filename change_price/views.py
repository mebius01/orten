from __future__ import unicode_literals
from django.shortcuts import render


def product_update(request):
	# some code
	ctx = {'data': 'test'}
	return render(request, 'product_update.html', ctx)