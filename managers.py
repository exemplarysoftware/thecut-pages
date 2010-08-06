from datetime import datetime
from django.db.models import Manager


class ActiveManager(Manager):
    """Returns only active (enabled, published) objects."""
    def active(self):
        queryset = self.get_query_set()
        return queryset.filter(is_enabled=True).filter(
            publish_at__lte=datetime.now())

