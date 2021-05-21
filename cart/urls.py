from django.urls import reverse
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('addtocart/<int:id>/', views.addtocart, name='addtocart'),
    path('delete_cart_item/<int:id>', views.delete_cart_item, name='delete_cart_item'),
    # path('checkout/', views.checkout_form, name='checkout'),
]
