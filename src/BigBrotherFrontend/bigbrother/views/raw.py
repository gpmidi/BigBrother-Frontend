''' Raw list of all actions/activities/logged events
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

@permission_required('Bbdata.can_view_full')
def list(req):
    """ Display a list of all known raw events """
    p = Paginator(Bbdata.objects.all().order_by('-pk'), 100)
    try:
        page = int(req.GET.get('page', 1))
    except ValueError:
        page = 1
    try:
        d = p.page(page)
    except (EmptyPage, InvalidPage):
        d = p.page(p.num_pages)
    return render_to_response(
                              'bigbrother/raw/list.html',
                              dict(
                                    page = d,
                                    ),
                              context_instance = RequestContext(req),
                              )

@permission_required('Bbdata.can_view_full')
def view(req, data_id):
    """ Display a raw event """
    data = get_object_or_404(Bbdata, pk = data_id)
    return render_to_response(
                              'bigbrother/raw/view.html',
                              dict(
                                    data = data,
                                    ),
                              context_instance = RequestContext(req),
                              )
    
    
