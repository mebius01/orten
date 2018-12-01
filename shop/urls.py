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
	# path('', views.category_list, name='category_list'),
	path('', views.product_list, name ='base'),
	# path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('tag/<tag_slug>/', views.product_list, name='list_product_by_tag'),
    # path('<product_slug>/', views.product_detail, name='product_detail'),
    path('category/', views.category, name ='list_category'),
    # path('category/<full_slug>/', views.category, name ='category'),
    re_path(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='show_category'),
    # re_path(r'^category/(?P<hierarchy>.+)/(?P<tag_slug>.+)/$', views.show_category, name='list_product_by_tag'),




	]