from django.db import models

# Create your models here.
class Delivery_Utilities(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

