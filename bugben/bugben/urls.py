from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mainsite.views.home', name='home'),
    url(r'^format/(?P<output_format>.+)$', 'mainsite.views.home', name='home'),
    url(r'^exoticaccess/doc/', include('django.contrib.admindocs.urls')),
    url(r'^exoticaccess/', include(admin.site.urls)),
)
