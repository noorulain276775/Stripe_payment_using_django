from datetime import MAXYEAR
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price =models.FloatField(null=True)
    active = models.BooleanField(null=True)
    image = models.ImageField(upload_to='products', null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class MyUser(AbstractUser):
    GENDER = [('Male', 'MALE'), ('Female', 'FEMALE')]
    date_of_birth = models.DateField()
    gender = models.CharField(choices=GENDER, max_length=7)


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    home_address = models.TextField(max_length=1000, null=True, blank=True)


    

