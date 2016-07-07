'''
Created on Mar 12, 2013

@author: giles
'''
from django.conf.urls import patterns, url

from ticket import views
from comments import views as cvs

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ticket_id>\d+)/$', views.detail),
    url(r'^(?P<ticket_id>\d+)/delete/$', views.delete),
    url(r'^(?P<ticket_id>\d+)/delete/real/$', views.delete_real),
    url(r'^(?P<ticket_id>\d+)/delete/fake/$', views.delete_fake),
    url(r'^new/$',views.newticket),
    url(r'^add/$',views.add),
    url(r'^comment/add/$',cvs.add)
    
)