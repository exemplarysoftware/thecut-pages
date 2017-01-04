# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, url
from thecut.pages import views


app_name = 'pages'


urlpatterns = [
    url(r'^(?P<slug>[\w/-]+)$', views.DetailView.as_view(),
        name='page_detail'),
]


