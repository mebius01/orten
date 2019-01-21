from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['delivery_method', 'pay_method', 'city', 'first_name', 'last_name', 'sur_name', 'email', 'mobile_phone', 'note_text']


