from django.db import models
from django.contrib.auth.models import User
from security.models import RetailerDetails
from staff.models import Medicine

# Create your models here.

class Feedback(models.Model):
    user=models.ForeignKey(RetailerDetails,on_delete=models.CASCADE)
    feedback=models.TextField()
    medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.last_name}"