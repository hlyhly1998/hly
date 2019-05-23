from django.db import models

# Create your models here.

class Wheel(models.Model):
    img = models.CharField(max_length=256)
    name = models.CharField(max_length=100)



class User(models.Model):

    name = models.CharField(max_length=100)

    password = models.CharField(max_length=256)

    email = models.CharField(max_length=100)

    token = models.CharField(max_length=256)