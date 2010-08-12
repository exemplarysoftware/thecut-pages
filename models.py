from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models
from pages.managers import PageManager

AttachedCallToAction = None
if 'ctas' in settings.INSTALLED_APPS:
    try:
        from ctas.models import AttachedCallToAction
    except ImportError:
        pass

MediaSet = None
if 'media' in settings.INSTALLED_APPS:
    try:
        from media.models import MediaSet
    except ImportError:
        pass


class AbstractPage(models.Model):
    """Abstract page model."""
    title = models.CharField(max_length=200)
    headline = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    
    publish_at = models.DateTimeField('Publish Date & Time')
    is_enabled = models.BooleanField(default=False,
        help_text='Is this page viewable on the website?')
    is_indexable = models.BooleanField(default=True,
        help_text='Should this page be indexed by search engines?')
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, editable=False,
        related_name='%(class)s_created_by_user')
    
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(User, editable=False,
        related_name='%(class)s_updated_by_user')
    
    objects = PageManager()
    
    class Meta:
        abstract = True
        get_latest_by = 'publish_at'
        ordering = ['title']
    
    def __unicode__(self):
        return self.title
   
    @property
    def is_active(self):
        return self in Page.objects.active().filter(pk=self.pk)
    
    @property
    def heading(self):
        return self.headline and self.headline or self.title
    
    @property
    def media(self):
        """Returns attached media set object.
        
        Convenience method/property for compatibility with 'media' app.
        
        """
        media = None
        if MediaSet:
            content_type = ContentType.objects.get_for_model(self)
            try:
                media = MediaSet.objects.get(content_type=content_type,
                object_id=self.id)
            except MediaSet.DoesNotExist:
                pass
        return media
    
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


class Page(AbstractPage):
    """Generic page."""
    site = models.ForeignKey(Site)
    url = models.CharField(max_length=100, db_index=True, unique=True,
        help_text='Example: /my-page')
    
    template = models.CharField(max_length=100, blank=True,
        help_text='Example: "pages/contact_page.html".')    
    
    class Meta(AbstractPage.Meta):
        unique_together = ['url', 'site']
    
    def get_absolute_url(self):
        return self.url

