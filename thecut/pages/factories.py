# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from thecut.publishing.factories import ContentFactory, ContentFakerFactory


class PageFactory(ContentFactory):

    FACTORY_FOR = 'pages.Page'


class PageFakerFactory(ContentFakerFactory):

    FACTORY_FOR = 'pages.Page'
