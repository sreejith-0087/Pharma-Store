from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class RetailerDetails(models.Model):
    id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=12,unique=True)
    photo=models.ImageField(upload_to='retailers')
    address=models.TextField(max_length=300)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"