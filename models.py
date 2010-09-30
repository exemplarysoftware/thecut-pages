from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models
from pages.decorators import attach_mediaset
from pages.utils import generate_unique_url
from thecut.managers import QuerySetManager
from thecut.models import AbstractSiteResource


AttachedCallToAction = None
if 'ctas' in settings.INSTALLED_APPS:
    try:
        from ctas.models import AttachedCallToAction
    except ImportError:
        pass


@attach_mediaset
class Page(AbstractSiteResource):
    """Generic page."""
    url = models.CharField(max_length=100, db_index=True,
        help_text='Example: /my-page')
    
    template = models.CharField(max_length=100, blank=True,
        help_text='Example: "pages/contact_page.html".')    
    
    objects = QuerySetManager()
    
    class Meta(AbstractSiteResource.Meta):
        unique_together = ['url', 'site']
    
    def get_absolute_url(self):
        return self.url
    
    def save(self, *args, **kwargs):
        if not self.url:
            self.url = generate_unique_url(self.title, Page,
                queryset=Page.objects.filter(site=self.site))
        super(Page, self).save(*args, **kwargs)
    
    @property
    def call_to_actions(self):
        """Returns queryset of any attached call-to-action objects.
        
        Convenience method/property for compatibility with 'ctas' app.
        
        """
        ctas = None
        if AttachedCallToAction:
            content_type = ContentType.objects.get_for_model(self)
            ctas = AttachedCallToAction.objects.active().filter(
                content_type=content_type, object_id=self.id)
        return ctas

