from django.shortcuts import render,redirect
from dashboard.models import Location, Hotel, Accomodation, Category, Transaction
from dashboard.views import id_generator
from dashboard.forms import BookingForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
from .access_token import lipa_na_mpesa
from django.views.decorators.csrf import csrf_exempt
import base64
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
import logging
from decimal import Decimal
logger = logging.getLogger(__name__)
from home.models import Booking

def site(request):
	hotels = Hotel.objects.all()
	loc  = Location.objects.all()
	return render(request, 'home/index.html',{'hotels':hotels,'loc':loc})


def view_package(request,urlhash):
	h = Hotel.objects.get(urlhash=urlhash)
	packages = Accomodation.objects.filter(hotel=h)
	hotels = Location.objects.all()
	cat = Category.objects.all()
	return render(request, 'home/package.html', {'packages': packages,'cat':cat,'hotels': hotels})


def expand_package(request, urlhash):
	package = Accomodation.objects.get(urlhash=urlhash)
	loc = Location.objects.get(name=package.hotel.location)
	return render(request, 'home/expand_package.html', {'package': package,'loc':loc})

def view_packages(request):
	packages = Accomodation.objects.all()
	hotels = Location.objects.all()
	cat = Category.objects.all()
	return render(request, 'home/package.html', {'packages': packages, 'cat': cat, 'hotels': hotels})


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
		prop = request.POST['prop']
		hotel = Hotel.objects.all().filter(location=loc)
		fn = Accomodation.objects.all().filter(cost__range=(mini, maxi)).filter(hotel__in=hotel)
		packages = fn.filter(category=prop)
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
	p = Accomodation.objects.get(urlhash=package)
	if request.method == 'POST':
		form = BookingForm(request.POST, request.FILES)
		types = request.POST.get('types')
		rooms = request.POST.get('rooms')
		if form.is_valid():
			if int(rooms) > 0:
				if int(rooms) > int(p.rooms):
					messages.info(request, "Sorry you have selected a number that is bigger than the rooms available.")
					return redirect('expand_package', urlhash=package)
				else:
					phone = form.cleaned_data['contact_phone']
					bal = int(p.cost)/int(p.rooms)*int(rooms)
					f = form.save(commit=False)
					f.urlhash = id_generator()
					instance = Accomodation.objects.get(urlhash=package)
					f.package = instance
					f.total = bal + int(types)
					f.save()
					messages.info(request, "Booking processed successfully.")
					return render(request, 'home/process_payment.html', {'total': f.total, 'id': f.id, 'phone': phone})
			else:
				phone = form.cleaned_data['contact_phone']
				f = form.save(commit=False)
				f.urlhash = id_generator()
				instance = Accomodation.objects.get(urlhash=package)
				f.package = instance
				f.total = int(p.cost) + int(types)
				f.save()
				messages.info(request, "Booking processed successfully.")
				return render(request, 'home/process_payment.html', {'total': f.total,'id':f.id,'phone': phone})
		else:
			return render(request, 'home/booking.html', {"form": form, 'package': p})
	else:
	    form = BookingForm()
	    args = {'form': form,'package':p}
	    return render(request, 'home/booking.html', args)


def stk_initiate(request):
	if request.method == "POST":
		phone = request.POST.get('phone')
		cost = request.POST.get('cost')
		i = request.POST.get('id')
		try:
			data = {"phone":phone,"amount":1,'id':i}
			lipa_na_mpesa(data)
			messages.info(request, "Payment Initiated.Check your phone and enter pin to confirm.")
			return HttpResponseRedirect('/')
		except:
			messages.info(request, "There was an issue processing the payment ,Please try again.")
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


@csrf_exempt
def process_lnm(request):
    con = json.loads(request.read().decode('utf-8'))
    con1 = con["Body"]
    data = con1["stkCallback"]
    update_data = dict()
    update_data['result_code'] = data['ResultCode']
    update_data['result_description'] = data['ResultDesc']
    update_data['checkout_request_id'] = data['CheckoutRequestID']
    update_data['merchant_request_id'] = data['MerchantRequestID']
    meta_data = data['CallbackMetadata']['Item']
    if len(meta_data) > 0:
        # handle the meta data
        for item in meta_data:
            if len(item.values()) > 1:
                key, value = item.values()
                if key == 'MpesaReceiptNumber':
                    update_data['mpesa_receipt_number'] = value
                if key == 'Amount':
                    update_data['amount'] = Decimal(value)
                    a = update_data['amount']
                if key == 'PhoneNumber':
                    update_data['phone'] = int(value)
                    p = update_data['phone']
                if key == 'TransactionDate':
                    date = str(value)
                    year, month, day, hour, min, sec = date[:4], date[4:-
                                                                      8], date[6:-6], date[8:-4], date[10:-2], date[12:]
                    update_data['transaction_date'] = '{}-{}-{} {}:{}:{}'.format(
                        year, month, day, hour, min, sec)
    v = Booking.objects.get(mpesa_receipt_code=data['CheckoutRequestID'])
    v.status = 1
    v.save()
    h = v.package.id
    s = Accomodation.objects.get(id=h)
    s.quantity-=1
    s.save()
    Transaction.objects.create(amount=update_data['amount'], phone=update_data['phone'], mpesa_receipt_number=update_data['mpesa_receipt_number'])
    message = {"ResultCode": 0, "ResultDesc": "The service was accepted successfully","ThirdPartyTransID": "traverse"}
    return JsonResponse({'message': message})

