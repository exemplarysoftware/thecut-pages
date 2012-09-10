# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.core.forms import ModelAdminForm
from thecut.pages.models import Page


class PageAdminForm(ModelAdminForm):
    class Meta(object):
        model = Page

