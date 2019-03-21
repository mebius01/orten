from django.urls import path
from .import views

app_name = 'order'
urlpatterns = [
	path('create/', views.order_create, name='order_create'),
	path('created/', views.order_created, name='order_created'),

]