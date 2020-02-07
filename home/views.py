from django.shortcuts import render
from dashboard.models import Location, Hotel, Accomodation
from dashboard.views import id_generator
from dashboard.forms import BookingForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

def site(request):
	hotels = Hotel.objects.all()
	loc  = Location.objects.all()
	return render(request, 'home/index.html',{'hotels':hotels,'loc':loc})


def view_package(request,urlhash):
	h = Hotel.objects.get(urlhash=urlhash)
	packages = Accomodation.objects.filter(hotel=h)
	return render(request, 'home/package.html', {'packages': packages})


def view_packages(request):
	packages = Accomodation.objects.all()
	return render(request, 'home/package.html', {'packages': packages})


def filter_packages(request):
	if request.method == "POST":
		search_text1 = request.POST['rooms']
		search_text2 = request.POST['hotels']
		search_text2 = request.POST['places']
		search_text3 = request.POST['start_date']
		search_text4 = request.POST['end_date']
		packages = Accomodation.objects.all().filter(rooms=search_text1)
		return render(request, 'home/package.html', {'packages': packages})
	else:
		return HttpResponseRedirect('/')

def booking(request,package):
	if request.method == 'POST':
		form = BookingForm(request.POST, request.FILES)
		if form.is_valid():
			p = form.save(commit=False)
			p.urlhash = id_generator()
			instance = Accomodation.objects.get(urlhash=package)
			p.package = instance
			p.save()
			messages.info(request, "Booking processed successfully.")
			return HttpResponseRedirect('/')
		else:
		    return render(request, 'home/booking.html', {"form": form})
	else:
	    form = BookingForm()
	    args = {'form': form}
	    return render(request, 'home/booking.html', args)
