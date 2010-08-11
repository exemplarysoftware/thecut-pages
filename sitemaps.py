from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from pages.models import Page


class PageSitemap(Sitemap):
    """Sitemaps.org XML sitemap."""
    def items(self):
        site = Site.objects.get_current()
        return Page.objects.active().filter(site=site)
    
    def lastmod(self, obj):
        return obj.updated_at

sitemaps = {'pages': PageSitemap}

