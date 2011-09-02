# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_protect
from django.views.generic.list_detail import object_detail
from thecut.pages.models import Page, SitesPage


@csrf_protect
def page(request, url):
    """Wrapper for page_detail view."""
    return page_detail(request, url)


def page_detail(request, url, queryset=None, **kwargs):
    if queryset is None:
        queryset = Page.objects.current_site().active().filter(url=url) \
            or SitesPage.objects.current_site().active().filter(url=url)
    
    kwdefaults = {'slug': url, 'slug_field': 'url',
        'template_name_field': 'template',
        'template_object_name': 'page'}
    kwdefaults.update(kwargs)
    
    return object_detail(request, queryset, **kwdefaults)

