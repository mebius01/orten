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


app_name = 'shop'

urlpatterns = [
    path('test/', test, name='test'),
    path('', Home.as_view(), name='home'),
    path('googledd11b6ee42c918f5.html', search_console, name='search_console'),
    path('contact/', Contact.as_view(), name='contact'),
    path('delivery_payment/', DeliveryPayment.as_view(), name='delivery_payment'),
    path('about/', About.as_view(), name='about'),
    path('shop/product/', product_list, name ='product_list'),
    # path('shop/product', ProductList.as_view(), name='product_list'),
    path('category/', Categories.as_view(), name ='category'),
    path('polygraphy/', Polygraphy.as_view(), name='polygraphy'),
    path('service/<slug:slug>', ServiceDetail.as_view(), name='service_detail'),
    path('shop/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('polygraphy/<int:pk>/', PolygraphyDetail.as_view(), name='polygraphy_detail'),
    re_path(r'^category/(?P<hierarchy>.+)/$', list_category, name='list_category'),
    ]
# from django.contrib.flatpages import views

# urlpatterns += [
#     path('polygraphy/vizitka/', flatpage, {'url': '/vizitka/'}, name='polygraphy'),
#     path('polygraphy/kalendari/', views.flatpage, {'url': '/kalendari/'}, name='k'),

# ]
 #    path('tag/<tag_id>/', views.product_list, name='list_product_by_tag'),
