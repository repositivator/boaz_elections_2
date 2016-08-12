from django.conf.urls import url, include
from django.contrib import admin
from . import views 

app_name='elections'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^areas/(?P<area>[a-zA-Z]+)/$', views.areas), 
    url(r'^areas/(?P<area>[a-zA-Z]+)/results/$', views.results), 
    url(r'^polls/(?P<poll_id>\d+)/$', views.polls),
    url(r'^candidate/(?P<name>[a-zA-Z]+)/$', views.candidates),
]
