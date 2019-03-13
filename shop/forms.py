from django import forms
from .models import Product
from watson import search as watson
class FilterForm(forms.Form):
	l=[]
	for i in Product.objects.all():
		l.append((i.vendor, i.vendor))
		if ('', '') in l:
			l.remove(('', ''))
	vendor = forms.ChoiceField(choices=l, label='vendor')