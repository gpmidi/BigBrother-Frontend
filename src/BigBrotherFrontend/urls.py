'''
Created on Feb 26, 2011

@author: gpmidi
'''
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^bigbrother/', include('BigBrotherFrontend.bigbrother.urls')),
    
    # Root page
    (r'^(?:/)$', 'BigBrotherFrontend.bigbrother.views.index.index'),
    (r'^index(?:/)$', 'BigBrotherFrontend.bigbrother.views.index.index'),
    (r'^index.html(?:/)$', 'BigBrotherFrontend.bigbrother.views.index.index'),
    
    # Account junk
    (r'^accounts/login(?:/)?$', 'django.contrib.auth.views.login', dict(redirect_field_name = '/index.html')),
    (r'^accounts/logout(?:/)?$', 'django.contrib.auth.views.logout_then_login'),
    # Let users edit their profile
    (r'^accounts/profile(?:/)?$', 'BigBrotherFrontend.bigbrother.views.profile.edit'),
    # Let users change their password
    (r'^accounts/changepassword(?:/)?$', 'django.contrib.auth.views.password_change'),
    (r'^accounts/password/done(?:/)?$', 'django.contrib.auth.views.password_change_done'),
    # Password reset
    (r'^password_reset(?:/)?$', 'django.contrib.auth.views.password_reset'),
    (r'^password_reset/done(?:/)?$', 'django.contrib.auth.views.password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)(?:/)?$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done(?:/)?$', 'django.contrib.auth.views.password_reset_complete'),
    # User registration
    (r'^accounts/register(?:/)?$', 'BigBrotherFrontend.bigbrother.views.profile.register'),
    (r'^accounts/confirm/([a-zA-Z0-9]+)(?:/)?$', 'BigBrotherFrontend.bigbrother.views.profile.confirm'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
