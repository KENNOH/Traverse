from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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
        return self.urlhash

class Accomodation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    urlhash = models.CharField(max_length=6, blank=True, null=True)
    rooms = models.CharField(max_length=255, blank=True, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    people  = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    cost = models.FloatField(default=0.0)
    status = models.NullBooleanField(max_length=5, default=0, verbose_name="Available")
    image = models.ImageField(upload_to='dashboard', blank=True, null=True)
    
    def __str__(self):
        return self.urlhash
