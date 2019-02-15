from django.contrib.sitemaps import Sitemap
from shop.models import Product, Category, Services

class ProductSitemap(Sitemap):
	priority = 1.0
	changefreq = 'daily'
	def items(self):
		return Product.objects.all()

class CategorySitemap(Sitemap):
	priority = 0.5
	changefreq = 'weekly'
	def items(self):
		return Category.objects.all()

class ServicesSitemap(Sitemap):
	priority = 1.0
	changefreq = 'weekly'
	def items(self):
		return Services.objects.all()