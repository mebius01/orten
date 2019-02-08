from django.shortcuts import render
from search.documents import ProductDocument
from elasticsearch_dsl import Search, Q

def search(request):
    q = request.GET.get('q')
    if q:
        products = ProductDocument.search().query("match", name=q)
    else:
        products = ''
    return render(request, 'search.html', {'products': products})
