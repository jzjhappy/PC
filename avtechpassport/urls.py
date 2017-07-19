'''
Created on May 29, 2017

@author: jwang02
'''
from django.conf.urls import url
from avtechpassport import views as  avtechpassport_views

urlpatterns = [
    url(r'^$', avtechpassport_views.index, name='index'),
    url(r'^schedule', avtechpassport_views.schedule, name='schedule'),
]

