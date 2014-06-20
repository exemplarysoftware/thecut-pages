# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.pages import views

try:
    from django.conf.urls import include, patterns, url
except ImportError:
    # Pre-Django 1.4 compatibility
    from django.conf.urls.defaults import include, patterns, url


urls = patterns(
    'thecut.pages.views',

    url(r'^(?P<slug>[\w/-]+)$', views.DetailView.as_view(),
        name='page_detail'),

)

urlpatterns = patterns('', (r'^', include(urls, namespace='pages')))
