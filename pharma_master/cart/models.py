from django.db import models
from staff.models import Medicine
from shop.models import RetailerDetails
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(RetailerDetails,on_delete=models.CASCADE)
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['date_added']
    def __str__(self):
        return '{}'.format(self.cart_id)

class CartItem(models.Model):
    product=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='CartItem'
    def sub_total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return '{}'.format(self.product)


class Orders(models.Model):
    user=models.ForeignKey(RetailerDetails,on_delete=models.CASCADE)
    delivery_status=models.BooleanField(default=False)
    date_time=models.DateTimeField(auto_now=True)
    amount=models.DecimalField(max_digits=8,decimal_places=2,default=0.00)

class ProductOrders(models.Model):
    order=models.ForeignKey(Orders,on_delete=models.CASCADE)
    product=models.ForeignKey(Medicine,on_delete=models.PROTECT)
    quantity=models.IntegerField()