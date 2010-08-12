from datetime import datetime
from django.db.models import Manager


class PageManager(Manager):
    def active(self):
        """Return active (enabled, published) objects."""
        queryset = self.get_query_set()
        return queryset.filter(is_enabled=True).filter(
            publish_at__lte=datetime.now())
    
    def sitemaps(self):
        """Return active, indexable objects for inclusion in sitemaps."""
        queryset = self.active()
        return queryset.filter(is_indexable=True)

