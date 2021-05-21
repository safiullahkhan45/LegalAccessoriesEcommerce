from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from store.models import Product
from users.models import Account
from datetime import datetime
# Create your views here.

def cart(request):

	# request.session.set_expiry(3)
	request.session.set_expiry(86400)
	try:
		cart_id = request.session['cart_id']
	
	except:
		cart_id = None

	if cart_id:
		
		if request.session['total_products'] == 0:
			context = {'empty': True}

		else:
			cart = Cart.objects.get(id = cart_id)
			context = {'cart': cart}

	else:
		context = {'empty': True}

	return render(request, 'cart/cart.html', context)


def addtocart(request, id):
	# person = Account.objects.get(username=request.user.username)
	size = request.GET.get('size')

	try:
	    cart_id = request.session['cart_id']
	except:
	    new_cart = Cart()
	    new_cart.save()
	    request.session['cart_id'] = new_cart.id
	    cart_id = new_cart.id

	cart = Cart.objects.get(pk = cart_id)

	product = Product.objects.get(pk = id)

	try:
		cartitem = CartItem.objects.get(cart=cart, product=product, size=size)
		cartitem.quantity += 1
		cartitem.total_cost += product.price
		cart.total_products += 1

	except:
		cartitem = CartItem(
					cart = cart,
					product = product,
					total_cost = product.price,
					size = size,
				)
		cart.total_products += 1
	cartitem.save()

	# cart.cart_item.add(cartitem)
	cart.total_amount += cartitem.product.price
	cart.save()
	request.session['total_products'] = cart.total_products

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	# return redirect('cart')

def delete_cart_item(request, id):
	cart_id = request.session['cart_id']
	cart = Cart.objects.get(pk = cart_id)
	cartitem = CartItem.objects.get(pk=id)
	print(cartitem.quantity)
	cart.total_products -= cartitem.quantity
	cart.total_amount -= cartitem.total_cost
	request.session['total_products'] -= cartitem.quantity
	cartitem.delete()
	cart.save()

	return redirect('cart')

# @login_required
# def checkout_form(request):

#     return render(request, 'cart/checkout.html')