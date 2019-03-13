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
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page


app_name = 'shop'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('delivery_payment/', views.delivery_payment, name='delivery_payment'),
    path('about/', views.about, name='about'),
    path('shop/product/', views.product_list, name ='product_list'),
    path('category/', views.category, name ='category'),
    path('polygraphy/', views.polygraphy, name='polygraphy'),
    path('service/<slug>', views.service_detail, name='service_detail'),
    path('shop/<slug>/', views.product_detail, name='product_detail'),
    path('polygraphy/<flatpage_id>/', views.polygraphy_detail, name='polygraphy_detail'),
    re_path(r'^category/(?P<hierarchy>.+)/$', views.list_category, name='list_category'),
    ]
# from django.contrib.flatpages import views

# urlpatterns += [
#     path('polygraphy/vizitka/', views.flatpage, {'url': '/vizitka/'}, name='polygraphy'),
#     path('polygraphy/kalendari/', views.flatpage, {'url': '/kalendari/'}, name='k'),

# ]
 #    path('tag/<tag_id>/', views.product_list, name='list_product_by_tag'),
