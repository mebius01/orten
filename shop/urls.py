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


app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views._test),
	path('shop/product/', views.product_list, name ='product_list'),
    # path('search/', views.search, name='search'),
    path('shop/category/', views.category, name ='category'),
    path('tag/<tag_id>/', views.product_list, name='list_product_by_tag'),
    path('service/<slug>', views.service_detail, name='service_detail'),
    path('shop/<slug>/', views.product_detail, name='product_detail'),
    re_path(r'^shop/category/(?P<hierarchy>.+)/$', views.list_category, name='list_category'),

	]
