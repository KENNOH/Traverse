from __future__ import absolute_import ,unicode_literals
import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A
from django.urls import reverse
from .models import Location, Hotel, Accomodation, Category 
from home.models import Booking


class ListingTable(tables.Table):
	#edit = tables.LinkColumn('accept',args=[A('pk')],verbose_name="Action",orderable=False,empty_values=())
	#editable =  CheckBoxColumnWithName(verbose_name="Select", accessor="pk")
	urlhash = tables.LinkColumn('hotel_expand', args=[A('pk')], verbose_name="Reference Code", orderable=True, empty_values=())
	# def render_edit(self,record):
	# 	if Document.objects.values_list('status',flat=True).get(order_number=record.pk)==False:
	# 		return format_html('<a href='+reverse("accept", args=[record.pk])+'><button type="button" class="form-control btn-success">Accept</button></a>')
	# 	else:
	# 		return format_html('<a href="#"><p>Accepted</p></a>')

	class Meta:
		model = Hotel
		fields = ('urlhash','name', 'location', 'contact_phone',
		          'contact_email', 'image', 'description','created_at')


class AccomodationTable(tables.Table):
	#edit = tables.LinkColumn('accept',args=[A('pk')],verbose_name="Action",orderable=False,empty_values=())
	#editable =  CheckBoxColumnWithName(verbose_name="Select", accessor="pk")
	urlhash = tables.LinkColumn('package_expand', args=[A('pk')], verbose_name="Reference Code", orderable=True, empty_values=())
	# def render_edit(self,record):
	# 	if Document.objects.values_list('status',flat=True).get(order_number=record.pk)==False:
	# 		return format_html('<a href='+reverse("accept", args=[record.pk])+'><button type="button" class="form-control btn-success">Accept</button></a>')
	# 	else:
	# 		return format_html('<a href="#"><p>Accepted</p></a>')

	class Meta:
		model = Accomodation
		fields = ('urlhash', 'hotel', 'rooms', 'cost',
		          'image', 'status', 'room_type','amenities', 'created_at')


class BookingTable(tables.Table):
	#edit = tables.LinkColumn('accept',args=[A('pk')],verbose_name="Action",orderable=False,empty_values=())
	#editable =  CheckBoxColumnWithName(verbose_name="Select", accessor="pk")
	#urlhash = tables.LinkColumn('service_expand', args=[A(
	#	'pk')], verbose_name="Reference Code", orderable=True, empty_values=())
	# def render_edit(self,record):
	# 	if Document.objects.values_list('status',flat=True).get(order_number=record.pk)==False:
	# 		return format_html('<a href='+reverse("accept", args=[record.pk])+'><button type="button" class="form-control btn-success">Accept</button></a>')
	# 	else:
	# 		return format_html('<a href="#"><p>Accepted</p></a>')

	class Meta:
		model = Booking
		fields = ('urlhash', 'name', 'contact_phone', 'contact_email', 'inquiry', 'package',
		          'total', 'status', 'mpesa_receipt_code', 'created_at')

