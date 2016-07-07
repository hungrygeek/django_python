'''
Created on 27 Mar 2013

@author: giles
'''

from django.conf.urls import patterns, url

from punts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<punt_id>\d+)/$', views.detail),
    
    
)