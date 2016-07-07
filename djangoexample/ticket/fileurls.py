'''
Created on Mar 13, 2013

@author: giles
'''
from django.conf.urls import patterns, url

from ticket import fileviews

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<ticket_id>\d+)/$', views.detail),
    #url(r'^new/$',views.newticket),
    url(r'^add/$',fileviews.add),
    
)