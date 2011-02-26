'''
Created on Feb 26, 2011

@author: gpmidi
'''
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('BigBrotherFrontend.bigbrother.views',
    (r'^raw(?:/)?$', 'raw.list'),
    (r'^raw/(\d+)(?:/)?$', 'raw.view'),
    
)
