from django.shortcuts import render
from dashboard.models import Location, Hotel, Accomodation
# Create your views here.

def site(request):
	hotels = Hotel.objects.all()
	loc  = Location.objects.all()
	return render(request, 'home/index.html',{'hotels':hotels,'loc':loc})
