from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^delete_hotel/(?P<pk>[0-9]+)/$',views.delete_hotel, name='delete_hotel'),
    url(r'^delete_package/(?P<pk>[0-9]+)/$',views.delete_package, name='delete_package'),
    url(r'^dashboard/generate_report/',views.generate_report, name='generate_report'),
    url(r'^dashboard/add/', views.add, name='add'),
    url(r'^dashboard/add_packages/', views.packages, name='packages'),
    url(r'^dashboard/listings/', views.listings, name='listings'),
    url(r'^dashboard/bookings/', views.bookings, name='bookings'),
    url(r'^dashboard/hotel_edit/(?P<pk>[0-9]+)/$',views.hotel_expand, name='hotel_expand'),
    url(r'^dashboard/package_edit/(?P<pk>[0-9]+)/$',views.package_expand, name='package_expand'),
    url(r'^dashboard/', views.dashboard, name='dashboard'), 
]
