from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

	# sur_name = forms.CharField(required=False)
	# note_text =  forms.CharField(required=False)

	class Meta:
		model = Order
		fields = ['delivery_method', 'pay_method', 'city', 'first_name', 'last_name', 'email', 'mobile_phone', 'note_text']


	# delivery_method = models.CharField(max_length=50, choices=DELIVERY_CHOICES, verbose_name='Спопсоб доставки', default=True)
	# pay_method = models.CharField(max_length=50, choices=PAY_CHOICES, verbose_name='Спопсоб оплаты', default=True)

	# last_name = models.CharField(verbose_name='Фамилия', max_length=50)
	# first_name = models.CharField(verbose_name='Имя', max_length=50)
	# sur_name = models.CharField(verbose_name='Отчесво', max_length=50)
	# city = models.CharField(verbose_name='Город', max_length=100)
	# department_np = models.CharField(verbose_name='НП №', max_length=300)

	# mobile_phone = models.CharField(max_length=15, verbose_name='Телефон')
	# email = models.EmailField(verbose_name='Email')
	# note_text =  models.TextField(blank=True, max_length=512, verbose_name='Дополнения, пожелания, заметки')

	# created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
	# updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
	# paid = models.BooleanField(verbose_name='Оплачен', default=False)