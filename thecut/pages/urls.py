# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, patterns, url
from thecut.pages import views


urls = patterns(
    'thecut.pages.views',

    url(r'^(?P<slug>[\w/-]+)$', views.DetailView.as_view(),
        name='page_detail'),

)

urlpatterns = patterns('', (r'^', include(urls, namespace='pages')))
