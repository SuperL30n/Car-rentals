from ast import mod
from email.policy import default
from hashlib import blake2b
from django.db import models
import os

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=255, null=False, blank=False)
    car_type = models.CharField(max_length=255, null=False, blank=False)
    car_image = models.ImageField(upload_to='../../tmp/upload/', null=True, blank=True)
    brief_description_of_the_car = models.TextField(max_length=1024, null=False, blank=False)
    car_category = models.CharField(max_length = 255, null=False, blank = False)
    no_of_seats = models.IntegerField(null=True, blank=True, default=1)
    amount_per_day = models.FloatField(default=5000, null=False, blank=False)
    car_availability = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    car_image_urls = models.URLField(null=False, blank=False, default="https://res.cloudinary.com/dxrxrd21n/image/upload/f_auto,q_auto/ooybbpi6zlzdllvuukuv")

    def __str__(self) -> str:
        return self.car_name

class Payments(models.Model):
    name = models.CharField(null=False, blank=False,max_length=1024)
    email_address = models.CharField(null=True, blank=False, max_length=255)
    phone_number= models.CharField(null=False,blank=False, max_length=1024)
    address = models.CharField(null=False,blank=False, max_length=2555)
    town_city= models.CharField(null=False, blank=False, max_length=1025)
    pickup_location = models.CharField(null=False, blank=False, max_length=2555)
    pickup_date = models.DateField(null=False, blank=False)
    dropoff_location = models.CharField(null=False, blank=False, max_length=2555)
    payment_ref = models.CharField(null=False, blank=False, default='',max_length=255)
    # dropoff_date = models.DateField(null=False, blank=False)
    number_of_days = models.IntegerField(null=False,blank=False, default=1)
    payment_amount = models.FloatField(null=False,blank=False)
    payment_date=models.DateField(auto_now_add=True)
    car_details = models.ForeignKey(Car, on_delete=models.CASCADE,null=False, blank=False)

    