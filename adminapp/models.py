from django.db import models

# Create your models here.
class Category(models.Model):
      category = models.CharField(max_length=10,default='')
      description = models.TextField()
      image=models.ImageField(upload_to='image',default='null.jpg')
class Product(models.Model):
      product = models.CharField(max_length=10,default='')
      price = models.IntegerField()
      category = models.CharField(max_length=10,default='')
      image=models.ImageField(upload_to='image',default='null.jpg')