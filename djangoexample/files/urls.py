'''
Created on Mar 13, 2013

@author: giles
'''
from django.conf.urls import patterns, url

from files import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<ticket_id>\d+)/$', views.detail),
    #url(r'^new/$',views.newticket),
    url(r'^add/$',views.add),
    
)