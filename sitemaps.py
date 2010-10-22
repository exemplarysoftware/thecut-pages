from django.contrib.sitemaps import Sitemap
from pages.models import Page, SitesPage


class PageSitemap(Sitemap):
    """Sitemaps.org XML sitemap."""
    def items(self):
        return Page.objects.current_site().indexable()
    
    def lastmod(self, obj):
        return obj.updated_at


class SitesPageSitemap(Sitemap):
    """Sitemaps.org XML sitemap."""
    def items(self):
        return SitesPage.objects.current_site().indexable()
    
    def lastmod(self, obj):
        return obj.updated_at

sitemaps = {'pages': PageSitemap, 'sitespages': SitesPageSitemap}

