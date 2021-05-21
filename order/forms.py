from django import forms
from users.models import Account


class CheckoutForm(forms.Form):

	city = forms.CharField(max_length=30)
	state = forms.CharField(max_length=30)
	postal_code = forms.CharField(max_length=30)
	email = forms.CharField(max_length=30)
	name = forms.CharField(max_length=30)
	delivery_address =forms.CharField(max_length=230)

	class Meta:

		fields = ['email', 'name', 'delivery_address', 'city', 'state', 'postal_code']
