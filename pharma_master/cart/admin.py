from django.contrib import admin
from cart.models import CartItem,Cart,Orders,ProductOrders
# Register your models here.

admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(ProductOrders)