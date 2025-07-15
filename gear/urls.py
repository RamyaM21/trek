from django.urls import path
from . import views

urlpatterns = [
    path('', views.gear_list, name='gear_list'),
    path('<int:gear_id>/', views.gear_detail, name='gear_detail'),
    path('checkout/<int:booking_id>/', views.checkout, name='gear_checkout'),
    path('confirmation/', views.order_confirmation, name='order_confirmation'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:gear_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    path('cart/checkout/', views.cart_checkout, name='cart_checkout'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('gear/place_order/', views.place_order, name='place_order'),
    path('gear/order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

