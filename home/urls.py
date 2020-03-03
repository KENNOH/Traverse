from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.site, name='site'), 
    url(r'^view_packages/', views.view_packages, name='view_packages'),
    url(r'^expand_package/(?P<urlhash>[0-9A-Za-z_\-]+)/$',views.expand_package, name='expand_package'),
    url(r'^filter_packages/', views.filter_packages, name='filter_packages'),
    url(r'^filter/', views.filt, name='filt'),
    url(r'^process_lnms/$', views.process_lnm, name='process_lnm'),
    url(r'^stk_initiate/', views.stk_initiate, name='stk_initiate'),
    url(r'^filtering_packages/', views.filtering_packages,name='filtering_packages'),
    url(r'^view_hotel_packages/(?P<urlhash>[0-9A-Za-z_\-]+)/$',views.view_package, name='view_package'),
    url(r'^booking/(?P<package>[0-9A-Za-z_\-]+)/$',views.booking, name='booking'),
    # url(r'^pets_display/', views.pets_display, name='pets_display'),
    # url(r'^pet_expand/(?P<urlhash>[0-9A-Za-z_\-]+)/$',views.pets_expand, name='pets_expand'),
    # url(r'^sort/(?P<name>[\w.@+-]+)', views.sort, name='sort'),
]
