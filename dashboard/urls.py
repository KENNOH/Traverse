from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^dashboard/add/', views.add, name='add'),
    url(r'^dashboard/add_packages/', views.packages, name='packages'),
    url(r'^dashboard/listings/', views.listings, name='listings'),
    url(r'^dashboard/bookings/', views.bookings, name='bookings'),
    url(r'^dashboard/', views.dashboard, name='dashboard'), 
]
