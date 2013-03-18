# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from thecut.pages import utils
from thecut.publishing.models import SiteContent


class AbstractPage(SiteContent):
    """Generic page."""

    url = models.CharField(max_length=100, db_index=True,
                           help_text='Example: /my-page')

    class Meta(SiteContent.Meta):
        abstract = True
        unique_together = ['url', 'site']

    def get_absolute_url(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = utils.generate_unique_url(
                self.title,
                queryset=self.__class__.objects.filter(site=self.site))
        if not self.url.startswith('/'):
            self.url = '/{0}'.format(self.url[:99])
        return super(AbstractPage, self).save(*args, **kwargs)


class Page(AbstractPage):

    pass
