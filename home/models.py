from django.db import models
from dashboard.models import Accomodation

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    urlhash = models.CharField(max_length=6, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    inquiry = models.CharField(max_length=255, blank=True, null=True)
    package = models.ForeignKey(Accomodation, on_delete=models.CASCADE)
    status = models.NullBooleanField(max_length=5, default=1, verbose_name="Payment status")
    inclusives = models.CharField(max_length=255, blank=True, null=True)
