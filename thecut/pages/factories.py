# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.publishing.factories import ContentFactory, ContentFakerFactory


class PageFactory(ContentFactory):

    class Meta(object):
        model = 'pages.Page'


class PageFakerFactory(ContentFakerFactory):

    class Meta(object):
        model = 'pages.Page'
