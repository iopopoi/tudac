from django.db import models

# Create your models here.

class Map_DB(models.Model):
    region = models.CharField(max_length=128)
    name= models.CharField(max_length=128)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude=models.DecimalField(max_digits=9, decimal_places=6)
    theme=models.CharField(null=True,max_length=128)

class Boring_DB(models.Model):
    todo = models.CharField(max_length=128)