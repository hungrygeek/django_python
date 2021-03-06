from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sjcpunts.views.home', name='home'),
    # url(r'^sjcpunts/', include('sjcpunts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^tickets/', include('ticket.urls')),
    url(r'^files/',   include('files.urls')),
    url(r'^users/',   include('members.urls')),
    url(r'^punts/',   include('punts.urls')),
    url(r'^comments/',include('comments.urls')),
    url(r'^$',       'sjcpunts.views.index'),
    url(r'^admin/',   include(admin.site.urls)),
    url(r'^login/', 'sjcpunts.views.mylogin'),
    url(r'^logout/','sjcpunts.views.mylogout')
)
