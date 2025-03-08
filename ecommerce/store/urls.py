from django.urls import path
from .views import (
    product_list, add_to_cart, view_cart, remove_from_cart, checkout,
    register, user_login, user_logout, product_detail, create_checkout_session
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('cart/', view_cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create-checkout-session/',create_checkout_session,name='create_checkout_session'),
]