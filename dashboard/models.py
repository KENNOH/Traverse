from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import string,random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))


class Location(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    urlhash = models.CharField(max_length=6, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    description  = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='dashboard', blank=True, null=True)


    def __str__(self):
        return self.name

d = id_generator()

class Accomodation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    urlhash = models.CharField(max_length=6)
    rooms = models.CharField(max_length=255, blank=True, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    #people  = models.IntegerField(blank=True, null=True)
    #location = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    cost = models.FloatField(default=0.0)
    status = models.NullBooleanField(max_length=5, default=1, verbose_name="Available")
    image = models.ImageField(upload_to='dashboard', blank=True, null=True)
    car_booking = models.CharField(max_length=10, default="0")
    flight_booking = models.CharField(max_length=10, default="0")


    def __str__(self):
        return self.urlhash
