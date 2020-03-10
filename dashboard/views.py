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
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
import os
from .render import Render
from django.template.loader import get_template
from xhtml2pdf import pisa
from .utils import render_to_pdf
from django.http import HttpResponse
import datetime
# Create your views here.

@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Property Owner').exists())
def dashboard(request):
	return render(request, 'dashboard/index.html')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))


def id_generator2(size=5, chars=string.ascii_uppercase):
		return ''.join(random.choice(chars) for _ in range(size))


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Property Owner').exists())
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
@user_passes_test(lambda u: u.groups.filter(name='Property Owner').exists())
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
@user_passes_test(lambda u: u.groups.filter(name='Property Owner').exists())
def listings(request):
	now = datetime.datetime.now()
	hotel = ListingTable(Hotel.objects.all().filter(user=request.user).order_by('-created_at'))
	RequestConfig(request, paginate={"per_page": 20}).configure(hotel)
	package = AccomodationTable(Accomodation.objects.all().filter(user=request.user).order_by('-created_at'))
	RequestConfig(request, paginate={"per_page": 20}).configure(package)
	return render(request, 'dashboard/listing.html', {'hotel': hotel,'package':package,'now':now})


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Property Owner').exists())
def bookings(request):
	acc = Accomodation.objects.all().filter(user=request.user)
	data = []
	for h in acc:
		data.append(h)
	bookings = BookingTable(Booking.objects.all().filter(package__in=data))
	RequestConfig(request, paginate={"per_page": 20}).configure(bookings)
	return render(request, 'dashboard/bookings.html', {'bookings': bookings})


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Property Owner').exists())
def hotel_expand(request, pk):
	hotel = Hotel.objects.get(pk=pk)
	if request.method == "POST":
		form = HotelForm(request.POST, request.FILES, instance=hotel)
		if form.is_valid():
			if bool(form.cleaned_data.get('attachment', False)) == False:
				form.save()
				messages.info(request, 'Updated successfully.')
				return HttpResponseRedirect('/dashboard/listings/')
			else:
				form.save()
				messages.info(request, 'Updated successfully.')
				return HttpResponseRedirect('/dashboard/listings/')
		else:
			form = HotelForm(request.POST, instance=hotel)
			args = {'form': form, 'pk': pk}
			messages.info(
				request, 'Sorry ,there are errors in your form, fix them to continue.')
			return render(request, 'dashboard/add.html', args)
	else:
		form = HotelForm(instance=hotel)
		args = {'form': form,'pk':pk}
		return render(request, 'dashboard/add.html', args)


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Property Owner').exists())
def package_expand(request, pk):
	package = Accomodation.objects.get(pk=pk)
	if request.method == "POST":
		form = AccomodationForm(request.POST, request.FILES, instance=package)
		if form.is_valid():
			if bool(form.cleaned_data.get('attachment', False)) == False:
				form.save()
				messages.info(request, 'Updated successfully.')
				return HttpResponseRedirect('/dashboard/listings/')
			else:
				form.save()
				messages.info(request, 'Updated successfully.')
				return HttpResponseRedirect('/dashboard/listings/')
		else:
			form = AccomodationForm(request.POST, instance=package)
			args = {'form': form, 'pk': pk}
			messages.info(request, 'Sorry ,there are errors in your form, fix them to continue.')
			return render(request, 'dashboard/packages.html', args)
	else:
		form = AccomodationForm(instance=package)
		args = {'form': form, 'pk': pk}
		return render(request, 'dashboard/packages.html', args)


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Property Owner').exists())
def delete_hotel(request,pk):
	hotel = Hotel.objects.get(pk=pk)
	os.remove(hotel.image.path)
	hotel.delete()
	messages.info(request, 'Hotel Listing deleted successfully.')
	return HttpResponseRedirect('/dashboard/listings/')
	

@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Property Owner').exists())
def delete_package(request, pk):
	acc = Accomodation.objects.get(pk=pk)
	os.remove(acc.image.path)
	acc.delete()
	messages.info(request, 'Item Listing deleted successfully.')
	return HttpResponseRedirect('/dashboard/listings/')


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='Property Owner').exists())
def generate_report(request):
	hidden = request.POST['hidden']
	now = datetime.datetime.now()
	d = id_generator2()
	n = str(request.user.first_name).split()[
	        0][0] + "." + str(request.user.last_name).split()[0][0]
	if hidden == 'bookings':
		acc = Accomodation.objects.all().filter(user=request.user)
		data = []
		for h in acc:
			data.append(h)
		bookings = Booking.objects.all().filter(package__in=data)
		template = get_template('dashboard/bookings_pdf.html')
		context = {'bookings': bookings, 'now': now, 'd': d, 'n': n}
		html = template.render(context)
		pdf = render_to_pdf('dashboard/bookings_pdf.html', context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Bookings.pdf"
			content = "inline; filename='%s'" % (filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" % (filename)
			response['Content-Disposition'] = content
			return response
		else:
			return HttpResponse("Not found")
