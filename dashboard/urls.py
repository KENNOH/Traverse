from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^dashboard/add/', views.add, name='add'),
    url(r'^dashboard/', views.dashboard, name='dashboard'), 
]
