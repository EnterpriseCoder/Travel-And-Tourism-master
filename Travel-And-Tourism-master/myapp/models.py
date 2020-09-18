from django.db import models
from django.urls import reverse

# Create your models here.
class Package(models.Model):
    destination = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    duration = models.CharField(max_length=256)
    dst_img = models.ImageField(upload_to='images/',blank=True)
    highlights = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.destination


class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=70)
    phone = models.PositiveIntegerField()
    desti = models.CharField(max_length=25)


class Auto(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=70)
    phone = models.PositiveIntegerField()
    pick = models.CharField(max_length=25)
    drop = models.CharField(max_length=25)
