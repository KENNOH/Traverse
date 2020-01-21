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
from dashboard.forms import HotelForm
# Create your views here.

def dashboard(request):
	return render(request, 'dashboard/index.html')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))


def add(request):
	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)
		if form.is_valid():
		    name = form.cleaned_data['name']
		    email = form.cleaned_data['contact_email']
		    phone = form.cleaned_data['contact_phone']
		    description = form.cleaned_data['description']
		    loc = form.cleaned_data['location']
		    image = form.cleaned_data['image']
		    rand = id_generator()
		    Hotel.objects.create(name=name, contact_email=email, image=image,
		                           contact_phone=phone, description=description, urlhash=rand, user=request.user, location=loc)
		    #for file in request.FILES.getlist("attachment"):
		    #    Images.objects.create(urlhash=rand,attachment=file)
		    messages.info(request, "Processed successfully.")
		    return HttpResponseRedirect('/dashboard/')
		else:
		    return render(request, 'dashboard/add.html', {"form": form})
	else:
	    form = HotelForm()
	    args = {'form': form}
	    return render(request, 'dashboard/add.html', args)
