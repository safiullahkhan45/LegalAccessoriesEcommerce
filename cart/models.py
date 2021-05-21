from django.db import models
from store.models import Product
# from users.models import Profile

# Create your models here.

class Cart(models.Model):
	total_products = models.IntegerField(default=0)
	total_amount = models.IntegerField(default=0)
	date_orderd = models.DateTimeField(auto_now=True)

	def __str__(self):
	    return str(self.id)


class CartItem(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	size = models.CharField(max_length=30, null=True, default=None)
	time_added = models.DateTimeField(auto_now=True, blank=True, null=True)
	quantity = models.IntegerField(default=1)
	total_cost = models.IntegerField(default=0)

	def __str__(self):
	    return str(f'{self.product.title} - {self.cart}')
