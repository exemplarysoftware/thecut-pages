# -*- coding: utf-8 -*-
from thecut.core.forms import ModelAdminForm
from thecut.pages.models import Page, SitesPage


class PageAdminForm(ModelAdminForm):
    class Meta:
        model = Page


class SitesPageAdminForm(ModelAdminForm):
    class Meta:
        model = SitesPage

