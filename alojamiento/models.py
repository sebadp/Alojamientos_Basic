from django.db import models
import datetime
# Create your models here.

class Booking(models.Model):
    name= models.CharField(max_length=100)
    tel = models.IntegerField()
    msg= models.TextField()

