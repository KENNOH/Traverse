from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.contrib.auth.models import User
import string,random
from .models import Location, Hotel, Accomodation
from dashboard.forms import HotelForm, AccomodationForm
from .tables import ListingTable,AccomodationTable,BookingTable
from home.models import Booking
from django_tables2 import RequestConfig
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def dashboard(request):
	return render(request, 'dashboard/index.html')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))


@login_required(login_url='/accounts/login/')
def add(request):
	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)
		if form.is_valid():
			h = form.save(commit=False)
			h.user = request.user
			h.urlhash = id_generator()
			h.save()
			messages.info(request, "Processed successfully.")
			return HttpResponseRedirect('/dashboard/listings/')
		else:
		    return render(request, 'dashboard/add.html', {"form": form})
	else:
	    form = HotelForm()
	    args = {'form': form}
	    return render(request, 'dashboard/add.html', args)


@login_required(login_url='/accounts/login/')
def packages(request):
	if request.method == 'POST':
		form = AccomodationForm(request.POST, request.FILES)
		if form.is_valid():
			p = form.save(commit=False)
			p.user = request.user
			p.urlhash = id_generator()
			p.save()
			messages.info(request, "Processed successfully.")
			return HttpResponseRedirect('/dashboard/listings/')
		else:
		    return render(request, 'dashboard/packages.html', {"form": form})
	else:
	    form = AccomodationForm()
	    args = {'form': form}
	    return render(request, 'dashboard/packages.html', args)


@login_required(login_url='/accounts/login/')
def listings(request):
	now = datetime.datetime.now()
	hotel = ListingTable(Hotel.objects.all().filter(user=request.user).order_by('-created_at'))
	RequestConfig(request, paginate={"per_page": 20}).configure(hotel)
	package = AccomodationTable(Accomodation.objects.all().filter(user=request.user).order_by('-created_at'))
	RequestConfig(request, paginate={"per_page": 20}).configure(package)
	return render(request, 'dashboard/listing.html', {'hotel': hotel,'package':package,'now':now})


@login_required(login_url='/accounts/login/')
def bookings(request):
	acc = Accomodation.objects.all().filter(user=request.user)
	bookings = BookingTable(Booking.objects.all())
	RequestConfig(request, paginate={"per_page": 20}).configure(bookings)
	return render(request, 'dashboard/bookings.html', {'bookings': bookings})
