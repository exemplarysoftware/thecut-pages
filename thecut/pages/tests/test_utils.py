# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from ..utils import generate_unique_url
from django.test import TestCase
from thecut.pages.models import Page
from thecut.pages.factories import PageFactory


class TestGenerateUniqueSlug(TestCase):

    """Test for utils.generate_unique_slug()"""

    def setUp(self):
        self.page = PageFactory(url='/blah')

    def test_generates_unique_slug_from_unique_text(self):
        """Test if a unique slug is generated from a unique string."""
        queryset = Page.objects.all()
        url = generate_unique_url(text='halb', queryset=queryset)
        self.assertFalse(Page.objects.filter(url=url))

    def test_generates_unique_slug_from_common_text(self):
        """Test if a unique slug is generated from a common string."""
        queryset = Page.objects.all()
        url = generate_unique_url(text=self.page.url,
                                  queryset=queryset)
        self.assertFalse(Page.objects.filter(url=url))
        self.assertEqual(url, '/1-blah')

    def test_generates_unique_slug_from_empty_string(self):
        """Test if a slug is generated from an empty string."""
        queryset = Page.objects.all()
        url = generate_unique_url(text='',
                                  queryset=queryset)
        self.assertFalse(Page.objects.filter(url=url))
