# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView
from thecut.pages.models import Page
from django.db.models import Q


class DetailView(DetailView):

    context_object_name = 'page'

    slug_field = 'url'

    template_name_field = 'template'

    def get_queryset(self):
        url = self.kwargs.get('slug', None)
        print("DetailView get_queryset url=", url)
        ret = Page.objects.current_site().active().filter(Q(url=url) |
                                                          Q(url=('/' + url)))
        print("DetailView get_queryset ret=", ret)
        return ret


@csrf_protect
def page(request, url):
    """Wrapper for page_detail view."""
    view = DetailView.as_view()
    return view(request, slug=url)
