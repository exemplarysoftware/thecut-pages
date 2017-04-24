# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from thecut.pages.factories import PageFactory
from thecut.pages.models import Page
from thecut.authorship.factories import UserFactory


class TestAbsoluteUrl(TestCase):
    def test_absolute_url(self):
        page = PageFactory(url='/blah')
        self.assertEqual(page.get_absolute_url(), '/blah')


class TestSavingPage(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_save_without_url(self):
        page = Page()
        page.title = 'biff'
        page.created_by = self.user
        page.updated_by = self.user
        page.save()

        page2 = Page.objects.get(pk=page.pk)
        self.assertEqual(page2.url, '/biff')

    def test_save_url_without_slash(self):
        page = Page()
        page.title = 'biff'
        page.url = 'biff'
        page.created_by = self.user
        page.updated_by = self.user
        page.save()

        page2 = Page.objects.get(pk=page.pk)
        self.assertEqual(page2.url, '/biff')

    def test_save_url_that_already_existis(self):
        page = PageFactory(url='/biff')
        page = Page()
        page.title = 'biff'
        page.created_by = self.user
        page.updated_by = self.user
        page.save()

        page2 = Page.objects.get(pk=page.pk)
        self.assertEqual(page2.url, '/1-biff')
