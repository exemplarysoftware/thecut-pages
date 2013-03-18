# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib.sitemaps import Sitemap
from thecut.pages.models import Page


class PageSitemap(Sitemap):
    """Sitemaps.org XML sitemap."""

    def items(self):
        return Page.objects.current_site().indexable()

    def lastmod(self, obj):
        return obj.updated_at


sitemaps = {'pages_page': PageSitemap}
