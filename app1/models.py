from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Table1(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    email=models.EmailField()
    place=models.CharField(max_length=20)
    password=models.CharField(max_length=8)

class Image(models.Model):
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    Place=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
    