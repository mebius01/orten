from django.contrib.sitemaps import Sitemap
from shop.models import Product, Category, Services
from django.urls import reverse

class ProductSitemap(Sitemap):
	priority = 1.0
	changefreq = 'daily'
	def items(self):
		return Product.objects.all()
	def location(self, item):
		return reverse('shop:product_detail', args=[item.slug])

class ServicesSitemap(Sitemap):
	priority = 1.0
	changefreq = 'weekly'
	def items(self):
		return Services.objects.all()
	def location(self, item):
		return reverse('shop:service_detail', args=[item.slug])

class CategorySitemap(Sitemap):
	priority = 0.5
	changefreq = 'weekly'
	def items(self):
		return Category.objects.all()
	def location(self, item):
		return reverse('shop:list_category', args=[item.get_absolute_url()])