from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about', views.about, name='about'),
	path('contact', views.contact, name='contact'),
	path('accessories', views.accessories, name='accessories'),
	path('courtwear', views.courtwear, name='courtwear'),
	path('ceremonials', views.ceremonials, name='ceremonials'),
	path('men', views.men, name='men'),
	path('women', views.women, name='women'),
	path('product_details/<int:id>', views.product_details, name='product_details'),
]