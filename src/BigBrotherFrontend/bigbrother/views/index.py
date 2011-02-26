'''
Created on Feb 26, 2011

@author: gpmidi
'''
from BigBrotherFrontend.bigbrother.models import *

from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.db.models import Q
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.decorators.cache import cache_page


def index(req):
    """ home page - do nothing for now """
    
    return render_to_response(
                              'bigbrother/index/index.html',
                              dict(
                                    ),
                              context_instance = RequestContext(req),
                              )
