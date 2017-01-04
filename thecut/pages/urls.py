# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, url
from thecut.pages import views


urls = [
    url(r'^(?P<slug>[\w/-]+)$', views.DetailView.as_view(),
        name='page_detail'),
]

urlpatterns = [include(urls, namespace='pages')]
