from django.db import models
from cart.models import Cart
from users.models import Account

# Create your models here.
class Order(models.Model):

	order_status_choices = (
			('Started', 'Started'),
			('Abandoned', 'Abandoned'),
			('InProgress', 'InProgress'),
			('Finished', 'Finished'),
		)

	cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
	order_id = models.CharField(max_length=100, unique=True)
	customer = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
	date_started = models.DateField(auto_now=True)
	status = models.CharField(max_length=20, choices=order_status_choices, default='Started')

	def __str__(self):
		return self.order_id

