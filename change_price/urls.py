from django.urls import path, include
from django.contrib.auth.decorators import user_passes_test

from change_price.views import product_update

urlpatterns = [
	path('product_update/', user_passes_test(lambda u: u.is_superuser)(product_update), name='product_update'),
]