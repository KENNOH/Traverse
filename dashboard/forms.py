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
from .models import Location, Hotel, Accomodation

class HotelForm(forms.ModelForm):
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
    location = forms.CharField(label='Location:', max_length=200, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control form-textbox'}))
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

class AccomodationForm(forms.ModelForm):
    name = forms.ModelChoiceField(label="Select Pet type:", required=True, queryset=Hotel.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'name': 'hotel'}))
    image = forms.ImageField(label="Attachment:", required=True, widget=forms.ClearableFileInput(
        attrs={'multiple': False, 'name': 'attachment'}))
    contact_email = forms.CharField(label='Contact Email:', max_length=200, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-textbox'}))
    contact_phone = forms.CharField(label='Contact Phone:', max_length=200, required=True,
                                    widget=forms.NumberInput(attrs={'class': 'form-control form-textbox'}))
    description = forms.CharField(label="Any Message?:", required=False, max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control form-textbox', 'name': 'description', 'rows': '4'}))
    location = forms.CharField(label='Location:', max_length=200, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control form-textbox'}))
    class Meta:
        model = Accomodation
        fields = ('name', 'location', 'contact_email',
                  'contact_phone','image', 'description')

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
