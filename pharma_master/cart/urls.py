from django.urls import path
from cart import views

app_name='cart'

urlpatterns=[
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('full_remove/<int:product_id>/',views.full_remove,name='full_remove'),
    path('checkout',views.Checkout,name='checkout'),
    path('place-order',views.PlaceOrder,name='place_order'),
    path('proceed-to-pay',views.razorpaycheck,name='proceed_to_pay'),

]