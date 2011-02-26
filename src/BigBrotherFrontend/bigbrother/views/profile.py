'''
Created on Feb 26, 2011

@author: gpmidi
'''
from BigBrotherFrontend.bigbrother.models import *
from BigBrotherFrontend.bigbrother.forms.profile import UserProfileForm
from BigBrotherFrontend.bigbrother.forms.registration import RegistrationForm

from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.db.models import Q
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponseServerError, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.decorators.cache import cache_page
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.hashcompat import md5_constructor
from django.template import resolve_variable
from django.core.cache import cache
from django.utils.http import urlquote

import datetime
import string
from random import choice

def generateRandomString(length = 12, chars = string.letters + string.digits):
    """ Returns a random string. """
    return ''.join([choice(chars) for i in range(length)])

@login_required
def edit(req):
    try:
        profile = req.user.get_profile()
        # FIXME: Catch the exact profile-not-found error
    except:
        profile = UserProfile(user = req.user)
        profile.save()
    
    if req.method == "POST":
        form = UserProfileForm(req.POST, instance = profile)
        if form.is_valid():
            req.user.first_name = form.cleaned_data['first_name']
            req.user.last_name = form.cleaned_data['last_name']
            req.user.email = form.cleaned_data['email']
            req.user.save()
            form.save()
            # Flush the CSS part so the settings take effect asap
            vary_on = [req.user.username, ]
            # Flush a few objects from django fragment cache
            args = md5_constructor(u':'.join([urlquote(var) for var in vary_on]))
            cache_key = 'template.cache.%s.%s' % ('css_random', args.hexdigest())
            cache.delete(cache_key)
            messages.success(req, 'Profile details updated. ')
        else:
            messages.info(req, 'No changes made - Invalid data')
    else:
        form = UserProfileForm(initial = dict(
                                    first_name = req.user.first_name,
                                    last_name = req.user.last_name,
                                    email = req.user.email,
                                    ),
                                instance = profile
                                )
    return render_to_response(
                              'lulz/profile/edit.html',
                              dict(
                                   form = form,
                                   ),
                              context_instance = RequestContext(req),
                              )

def register(req):
    """ Register a new account """
    if req.user.is_authenticated():
        return HttpResponseRedirect('/accounts/profile/')
    
    if req.POST:
        form = RegistrationForm(req.POST)
        if form.is_valid() and form.cleaned_data['password1'] == form.cleaned_data['password2']:
            user = User(
                      username = form.cleaned_data['username'],
                      email = form.cleaned_data['email'],
                      is_active = False,
                      )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            user.groups.add(
                            Group.objects.get(name = 'Normals')
                            )
            user.save()
            profile = UserProfile(
                                user = user,
                                activation_key = generateRandomString(32),
                                key_expires = datetime.datetime.now() + datetime.timedelta(days = 2),
                                )
            profile.save()
            message = '''
Hello, %s, and thanks for signing up for an                                                                                                    
lulzlunch.com account!

To activate your account, click this link 
within 48 hours:

http://%s/accounts/confirm/%s/
                ''' % (user.username, Site.objects.get_current().domain, profile.activation_key)
                
            send_mail(
                      'Your new mine.gpmidi.net account confirmation',
                      message,
                      'bounce@gpmidi.net',
                      [form.cleaned_data['email'], ],
                      )
            return render_to_response(
                              'bigbrother/profile/register_sent.html',
                              dict(
                                   ),
                              context_instance = RequestContext(req),
                              )
        else:
            pass
    else:
        form = RegistrationForm()
        
    return render_to_response(
                              'bigbrother/profile/register.html',
                              dict(
                                   form = form,
                                   ),
                              context_instance = RequestContext(req),
                              )

def confirm(req, key):
    profile = get_object_or_404(UserProfile, activation_key = key)
    user = profile.user
    user.is_active = True
    user.save()
    return render_to_response(
                              'bigbrother/profile/registered.html',
                              dict(
                                   nuser = user,
                                   ),
                              context_instance = RequestContext(req),
                              )
    

