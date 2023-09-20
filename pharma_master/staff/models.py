from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StaffDetails(models.Model):
    id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    photo=models.ImageField(upload_to='photos')
    address=models.TextField(max_length=200)
    resume=models.FileField(upload_to='resumes')
    join_date=models.DateField(auto_now=True)
    phone=models.CharField(max_length=10)
    manager=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

class Categories(models.Model):
    category=models.CharField(max_length=30,unique=True)
    link=models.SlugField(unique=True)
    def __str__(self):
        return self.category

class Brand(models.Model):
    brand=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.brand

class Medicine(models.Model):
    medicine=models.CharField(max_length=50,unique=True)
    content=models.CharField(max_length=200)
    description=models.TextField(max_length=1000,blank=True)
    category=models.ForeignKey(Categories,on_delete=models.PROTECT)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    brand=models.ForeignKey(Brand,on_delete=models.PROTECT)
    image=models.ImageField(upload_to='medicines')
    stock=models.IntegerField()


    def __str__(self):
        return self.medicine

class PendingOrders(models.Model):
    medicine=models.ForeignKey(Medicine,on_delete=models.PROTECT)
    count=models.IntegerField()

