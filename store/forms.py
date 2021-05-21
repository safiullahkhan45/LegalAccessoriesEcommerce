from django import forms
from .models import Product

class SizeForm(forms.ModelForm):

	class Meta:

		model = Product
		fields = ['size']


class ContactUsForm(forms.Form):

	name = forms.CharField(max_length=30)
	contact = forms.CharField(max_length=30)
	email = forms.CharField(max_length=30)
	subject = forms.CharField(max_length=30)
	message =forms.CharField(max_length=500)

	class Meta:

		fields = ['name', 'contact', 'email', 'subject', 'message']
