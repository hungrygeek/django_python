'''
Created on Mar 12, 2013

@author: giles
'''
from django.conf.urls import patterns, url

from comments import views

urlpatterns = patterns('',
    
    url(r'^add/$',views.add),
    url(r'^(?P<comment_id>\d+)/$', views.parent),
    
)