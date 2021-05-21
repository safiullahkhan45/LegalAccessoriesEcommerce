from django.db import models

# Create your models here.

class Size(models.Model):

	size = models.CharField(max_length=30)

	def __str__(self):
		return self.size

class OtherImages(models.Model):

	other_image = models.ImageField(upload_to='Store')


class Product(models.Model):
	category_choice = {
		('Accessories', 'Accessories'),
		('Courtwear', 'Courtwear'),
		('Ceremonial', 'Ceremonial'),
		('Men', 'Men'),
		('Women', 'Women')
	}

	category = models.CharField(max_length=20, choices=category_choice, default='Accessories')
	size = models.ManyToManyField(Size)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=300)
	price = models.IntegerField()
	image = models.ImageField(upload_to='Store')
	other_image = models.ManyToManyField(OtherImages, blank=True)

	def __str__(self):
		return self.title

		