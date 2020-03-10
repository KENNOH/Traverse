from django.contrib.auth.forms import UserChangeForm
import time
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.contrib.auth.models import Group
from .models import Location, Hotel, Accomodation,Category
from home.models import Booking

class HotelForm(forms.ModelForm):
    loc = Location.objects.all()
    name = forms.CharField(label='Name:', max_length=200, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-textbox'}))
    image = forms.ImageField(label="Attachment:", required=True, widget=forms.ClearableFileInput(
        attrs={'multiple': False, 'name': 'attachment'}))
    contact_email = forms.CharField(label='Contact Email:', max_length=200, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-textbox'}))
    contact_phone = forms.CharField(label='Contact Phone:', max_length=200, required=True,
                                    widget=forms.NumberInput(attrs={'class': 'form-control form-textbox'}))
    description = forms.CharField(label="Any Message?:", required=False, max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control form-textbox', 'name': 'description', 'rows': '4'}))
    location = forms.ModelChoiceField(label="Select Location:", queryset=loc, widget=forms.Select(
        attrs={'class': 'form-control', 'name': 'location'}))
    class Meta:
        model = Hotel
        fields = ('name', 'location', 'contact_email',
                  'contact_phone','image', 'description')

    def clean(self, *args, **kwargs):
        # contact_email = self.cleaned_data['contact_email']
        # if not contact_email:
        #     raise forms.ValidationError("Please a contact email.")
        return super(HotelForm, self).clean(*args, **kwargs)

    def save(self, commit=True):
        Document = super(HotelForm, self).save(commit=False)
        if commit:
            Document.save()
        return Document


class DateInput(forms.DateTimeInput):
	input_type = 'date'

class AccomodationForm(forms.ModelForm):
    CHOICES = (
        ("0","Not Available"),
        ("1","Available")
    )
    CHOICES2 = (
        ("Vip Class", "Vip Class"),
        ("Business Class", "Business Class"),
        ("Economy Class", "Economy Class"),
    )
    CHOICES3 = (
        ("Wi-FI", "Wi-FI"),
        ("Room Service", "Room Service"),
        ("Television and Home sound system", "Television and Home sound system"),
        ("Massage", "Massage"),
        ("Free drinks", "Free drinks"),
    )
    cat = Category.objects.all()
    category = forms.ModelChoiceField(label="Select item type:", queryset=cat, widget=forms.Select(
        attrs={'class': 'form-control', 'name': 'category'}))
    rooms = forms.CharField(label="Enter number of rooms per package:", required=True,widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'rooms'}))
    image = forms.ImageField(label="Image:", required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': False, 'name': 'attachment'}))
    cost = forms.IntegerField(label='Cost:', required=True,widget=forms.NumberInput(attrs={'class': 'form-control form-textbox'}))
    #quantity = forms.IntegerField(label='Available Number of packages:', required=True, widget=forms.NumberInput(attrs={'class': 'form-control form-textbox'}))
    check_in = forms.DateField(label='Available date:', required=True,widget=DateInput(attrs={'class': 'form-control form-textbox'}))
    check_out = forms.DateField(label='End date:', required=True,widget=DateInput(attrs={'class': 'form-control form-textbox'}))
    room_type = forms.ChoiceField(label="Select Room type:", required=True, choices=CHOICES2, widget=forms.Select(attrs={'class': 'form-control', 'name': 'room_type'}))
    amenities = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=CHOICES3)
    #flight_booking = forms.ChoiceField(label="Flight booking status:", required=True, choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'name': 'flight_booking'}))
    #car_booking = forms.ChoiceField(label="Car booking status:", required=True, choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'name': 'car_booking'}))

    class Meta:
        model = Accomodation
        fields = ('hotel', 'category', 'rooms', 'image', 'cost',
                  'room_type','amenities','check_in', 'check_out')

    def clean(self, *args, **kwargs):
        # contact_email = self.cleaned_data['contact_email']
        # if not contact_email:
        #     raise forms.ValidationError("Please a contact email.")
        return super(AccomodationForm, self).clean(*args, **kwargs)

    def save(self, commit=True):
        Document = super(AccomodationForm, self).save(commit=False)
        if commit:
            Document.save()
        return Document


class BookingForm(forms.ModelForm):
    OPTIONS = (
        ("Literature", "Literature"),
        ("Mathematics", "Mathematics"),
        ("Research Writing", "Research Writing"),
      	("Statistics", "Statistics"),
      	("Art", "Art"),)
    name = forms.CharField(label='Enter Full Names:', max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control form-textbox'}))
    contact_email = forms.CharField(label='Contact Email:', max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control form-textbox'}))
    contact_phone = forms.CharField(label='Contact Phone:', max_length=200, required=True,widget=forms.NumberInput(attrs={'class': 'form-control form-textbox'}))
    inquiry = forms.CharField(label="Remarks:", required=False, max_length=200, widget=forms.Textarea(attrs={'class': 'form-control form-textbox', 'name': 'description', 'rows': '4'}))
    
    class Meta:
        model = Booking
        fields = ('name','contact_email',
                  'contact_phone', 'inquiry')

    def clean(self, *args, **kwargs):
        # contact_email = self.cleaned_data['contact_email']
        # if not contact_email:
        #     raise forms.ValidationError("Please a contact email.")
        return super(BookingForm, self).clean(*args, **kwargs)

    def save(self, commit=True):
        Document = super(BookingForm, self).save(commit=False)
        if commit:
            Document.save()
        return Document
