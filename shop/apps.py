from django.apps import AppConfig
from watson import search as watson

class ShopConfig(AppConfig):
    name = 'shop'
    def ready(self):
        Product = self.get_model("Product")
        watson.register(Product)