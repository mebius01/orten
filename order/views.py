from django.shortcuts import render
from django.shortcuts import redirect
# from .tasks import order_created # for celery
from .tasks import email_customer # for dramatiq
# Create your views here.


from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
			cart.clear()
			# order_created.delay(order.id) # for celery
			email_customer(order.id) # for dramatiq
			# return render(request, 'order/created.html', {'order': order})
			return redirect('order:order_created')
	else:
		form = OrderCreateForm()
	return render(request, 'order/create.html', {'cart': cart, 'form': form})

def order_created(request):
	order=Order.objects.all().order_by('-created')[0]
	return render(request, 'order/created.html', {'order': order})