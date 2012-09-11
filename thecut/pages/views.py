# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.views.decorators.csrf import csrf_protect
from thecut.pages.models import Page

# Class-based views
from distutils.version import StrictVersion
from django import get_version
if StrictVersion(get_version()) < StrictVersion('1.3'):
    import cbv as generic
else:
    from django.views import generic


class DetailView(generic.DetailView):
    context_object_name = 'page'
    slug_field = 'url'
    template_name_field = 'template'
    
    def get_queryset(self):
        url = self.kwargs.get('slug', None)
        return Page.objects.current_site().active().filter(url=url)


@csrf_protect
def page(request, url):
    """Wrapper for page_detail view."""
    view = DetailView.as_view()
    return view(request, slug=url)

