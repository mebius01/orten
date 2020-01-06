"""orten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from shop.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView, DetailView


app_name = 'shop'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name = 'about.html'), name='about'),
    path('delivery_payment/', TemplateView.as_view(template_name = 'delivery_payment.html'), name='delivery_payment'),
    path('contact/', TemplateView.as_view(template_name = 'contact.html'), name='contact'),
    path('category/', TemplateView.as_view(template_name = 'shop/category.html'), name ='category'),
    path('polygraphy/', TemplateView.as_view(template_name = "shop/polygraphy.html"), name='polygraphy'),
    path('googledd11b6ee42c918f5.html', TemplateView.as_view(template_name = 'googledd11b6ee42c918f5.html'), name='search_console'),
    path('shop/product/', ProductList.as_view(), name ='product_list'),
    # path('shop/product/', product_list, name ='product_list'),
    path('service/<slug:slug>', DetailView.as_view(model = Services, template_name = 'shop/service_detail.html'), name='service_detail'),
    path('shop/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('polygraphy/<int:pk>/', DetailView.as_view(model = Polygraphy,	template_name = 'shop/polygraphy_detail.html'), name='polygraphy_detail'),
    path('category/<path:path>/', ListCategory.as_view(), name='list_category'),
    ]
