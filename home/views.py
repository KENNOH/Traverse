from django.shortcuts import render,redirect
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


def expand_package(request, urlhash):
	package = Accomodation.objects.get(urlhash=urlhash)
	loc = Location.objects.get(name=package.hotel.location)
	return render(request, 'home/expand_package.html', {'package': package,'loc':loc})

def view_packages(request):
	packages = Accomodation.objects.all()
	hotels = Location.objects.all()
	return render(request, 'home/package.html', {'packages': packages,'hotels':hotels})


def filter_packages(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
		hotel = Hotel.objects.all().filter(name=search_text)
		packages = Accomodation.objects.all().filter(hotel__in=hotel)
		return render(request, 'home/filter_item.html', {'packages': packages})
	else:
		return HttpResponseRedirect('/')
	
def filt(request):
	if request.method == "POST":
		maxi = request.POST['max']
		mini = request.POST['min']
		loc = request.POST['loc']
		hotel = Hotel.objects.all().filter(location=loc)
		packages = Accomodation.objects.all().filter(cost__range=(mini, maxi)).filter(hotel__in=hotel)
		hotels = Location.objects.all()
		return render(request, 'home/package.html', {'packages': packages, 'hotels': hotels})
	else:
		return HttpResponseRedirect('/')


def filtering_packages(request):
	if request.method == "POST":
		loc = request.POST['search_text']
		packages = Accomodation.objects.all().filter()
		hotels = Location.objects.all()
		hotel = Hotel.objects.all().filter(location=loc)
		packages = Accomodation.objects.all().filter(hotel__in=hotel)
		return render(request, 'home/package.html', {'packages': packages, 'hotels': hotels})
	else:
		return HttpResponseRedirect('/')

def booking(request,package):
	one = request.POST.get('types')
	p = Accomodation.objects.get(urlhash=package)
	if request.method == 'POST':
		form = BookingForm(request.POST, request.FILES)
		if form.is_valid():
			total = request.POST.get('total')
			phone = form.cleaned_data['contact_phone']
			p = form.save(commit=False)
			p.urlhash = id_generator()
			instance = Accomodation.objects.get(urlhash=package)
			p.package = instance
			p.save()
			messages.info(request, "Booking processed successfully.")
			return render(request, 'home/process_payment.html', {'total': total, 'phone': phone})
		else:
			price = int(one) + int(p.cost)
			return render(request, 'home/booking.html', {"form": form, 'package': p,'price':price})
	else:
	    form = BookingForm()
	    price = int(one) + int(p.cost)
	    args = {'form': form,'package':p,'price':price}
	    return render(request, 'home/booking.html', args)

def process_payment(request,data):
	phone = data.get('phone')
	total = data.get('total') 		
	return render(request, 'home/process_payment.html', {'total': total,'phone':phone})
