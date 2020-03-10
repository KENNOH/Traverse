from django.db import models
from dashboard.models import Accomodation

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    urlhash = models.CharField(max_length=6, blank=True, null=True,verbose_name="Unique Id")
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    inquiry = models.CharField(max_length=255, blank=True, null=True)
    package = models.ForeignKey(Accomodation, on_delete=models.CASCADE, verbose_name="PackageId")
    status = models.NullBooleanField(max_length=5, default=1, verbose_name="Payment status")
    total = models.FloatField(max_length=255, blank=True, null=True)
    status = models.NullBooleanField(max_length=5, default=0, verbose_name="Payment status")
    mpesa_receipt_code = models.CharField(max_length=255, blank=True, null=True)
