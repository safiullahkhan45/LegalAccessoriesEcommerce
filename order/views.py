from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import time, datetime
from cart.models import Cart
from . models import Order
from . forms import CheckoutForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
@login_required
def checkout(request):

	start_time = time.time()

	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(pk = cart_id)

	except:
		return redirect('cart')

	try:
		order = Order.objects.get(cart = cart)
	except:
		# print(datetime.date.today())
		order = Order(
				cart = cart,
				customer = request.user,
				order_id = f'{request.user.username} - {datetime.date.today()}'
			)
		order.save()

	print(request.user.email)

	form = CheckoutForm()

	if request.method == 'POST':

		form = CheckoutForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			name = form.cleaned_data.get('name')
			delivery_address = form.cleaned_data.get('delivery_address')
			city = form.cleaned_data.get('city')
			state = form.cleaned_data.get('state')
			postal_code = form.cleaned_data.get('postal_code')

			print(postal_code)

			subject = f'Order Details: {order.order_id}'
			message = 'Following are the order details.\n'
			email_from = settings.EMAIL_HOST_USER
			email_to = [request.user.email]

			for item in order.cart.cartitem_set.all():
				message += f'{item.product.title} - {item.quantity} - {item.size}'
				message += '\n'

			message += f'Total Products - {order.cart.total_products}'
			message += '\n'
			message += f'Total Amount - {order.cart.total_amount}'
			message += '\n'

			print('before email')

			# print(message)

			send_mail(
				subject,
				message,
				email_from,
				email_to,
				fail_silently=False,
			)

			order.status = 'InProgress'
			order.save()

		return redirect('home')

	context = {
		'order': order,
	}

	return render(request, 'order/checkout.html', context)
