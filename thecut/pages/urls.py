# -*- coding: utf-8 -*-
from django.conf.urls.defaults import include, patterns, url
from thecut.pages import views


urls = patterns('thecut.pages.views',
    url(r'^(?P<slug>[\w/-]+)$', views.DetailView.as_view(), name='page_detail'),
)

urlpatterns = patterns('',
    (r'^', include(urls, namespace='pages')),
)

