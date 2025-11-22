from django.db import models

from adminapp.models import Product

# Create your models here.
class Contact(models.Model):
      yourname =  models.CharField(max_length=100)
      youremail= models.EmailField(null=True)
      phone = models.CharField(max_length=100)
      subject = models.CharField(max_length=100)
      message = models.TextField(default='')
class Registration(models.Model):
      username =  models.CharField(max_length=100)
      password = models.CharField(max_length=100,default='')
      email= models.EmailField(null=True)
      phone = models.CharField(max_length=100)
class Cart(models.Model):
      cartuser = models.ForeignKey(Registration,on_delete=models.CASCADE)
      cartproduct = models.ForeignKey(Product,on_delete=models.CASCADE)
      quantity = models.IntegerField()
      total = models.IntegerField()
      status = models.IntegerField(default=0)
class Checkout(models.Model):
      usercheckout = models.ForeignKey(Registration,on_delete=models.CASCADE)
      checkoutcart = models.ForeignKey(Cart,on_delete=models.CASCADE)
      address = models.CharField(max_length=20)
      city = models.CharField(max_length=20)
      country = models.CharField(max_length=20)
      postcode = models.CharField(max_length=20)