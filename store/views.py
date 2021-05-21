from django.shortcuts import render, redirect
from . models import Product
from . forms import SizeForm, ContactUsForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):

	context = {}

	return render(request, 'store/home.html', context)


def about(request):

	context = {}

	return render(request, 'store/about.html', context)


def accessories(request):

	obj = Product.objects.filter(category = 'Accessories')

	context = {
		'obj': obj,
	}

	return render(request, 'store/accessories.html', context)


def courtwear(request):

	obj = Product.objects.filter(category = 'Courtwear')

	context = {
		'obj': obj,
	}

	return render(request, 'store/courtwear.html', context)


def ceremonials(request):

	obj = Product.objects.filter(category = 'Ceremonials')

	context = {
		'obj': obj,
	}

	return render(request, 'store/ceremonials.html', context)


def men(request):

	obj = Product.objects.filter(category = 'Men')

	context = {
		'obj': obj,
	}

	return render(request, 'store/men.html', context)


def women(request):

	obj = Product.objects.filter(category = 'Women')

	context = {
		'obj': obj,
	}

	return render(request, 'store/women.html', context)


def product_details(request, id):

    obj = Product.objects.get(pk=id)
    # if request.method == 'GET':
    # 	form = SizeForm()

    context = {
    	'obj': obj
    }

    return render(request, 'store/product_details.html', context)

def contact(request):

	form = ContactUsForm()

	if request.method == 'POST':

		form = ContactUsForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			email = form.cleaned_data.get('email')
			contact = form.cleaned_data.get('contact')
			subject = form.cleaned_data.get('subject')
			message = form.cleaned_data.get('message')

			subject = f'Legal Accessories Query - {subject}'
			send_message = f'Name: {name} \n'
			send_message += f'Phone Number: {contact} \n'
			send_message += f'Email: {email} \n\n'
			send_message += message
			email_from = settings.EMAIL_HOST_USER
			email_to = ['safiullah.khan145@gmail.com']

			print('before email')

			# print(message)

			send_mail(
				subject,
				send_message,
				email_from,
				email_to,
				fail_silently=False,
			)

		return redirect('home')

	context = {
		'form': form
	}

	return render(request, 'store/contact.html', context)
