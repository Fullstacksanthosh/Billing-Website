from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Productdetail(models.Model):
    productname = models.CharField(null=False,max_length=25)
    price = models.IntegerField(null=False)
    
    
    
    def __str__(self):
        return self.productname
    
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False,max_length=30)
    email = models.TextField(null=False,max_length=30)
    Phonenumber = models.IntegerField(null=False)
    datecreated = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    fullname = models.TextField(null=False)
    PhoneNumber = models.IntegerField(null=False)
    Emailaddress = models.TextField(null=False)
    Doorno = models.TextField(null=False)
    Streetname = models.TextField(null=False)
    Cityname = models.TextField(null=False)
    Productdetails = models.ImageField(null=False)
    
    
    def __str__(self):
        return self.fullname
    
    
class Status(models.Model):
    fullname = models.TextField(null=False)
    Email = models.TextField(null=False)
    Phonenumber = models.IntegerField(null=False)
    Orderedon = models.DateField(null=False)
    Deliveredon = models.DateField(null=False)
    
    
    def __str__(self):
        return self.fullname
    