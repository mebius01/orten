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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ProductSitemap, CategorySitemap, ServicesSitemap
# from django.conf.urls import handler404, handler500
from shop.views import handler404, handler500


sitemaps = {'product': ProductSitemap, 'category': CategorySitemap, 'services': ServicesSitemap}

if settings.DEBUG:
    import debug_toolbar
urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    # path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico'), name='favicon'),
    path('', include('shop.urls')),
    # path('polygraphy/', include('django.contrib.flatpages.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404='shop.views.handler404'
handler500='shop.views.handler500'
