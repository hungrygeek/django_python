'''
Created on 26 Mar 2013

@author: giles
'''
from django.conf.urls import patterns, url

from comments import views as cvs
from members import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<username>\w+)/$', views.detail),
    url(r'^comment/add/$',cvs.add),
    url(r'^$', views.index)
    
)