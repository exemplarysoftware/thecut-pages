# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from django.core.management.base import CommandError
from thecut.pages.models import Page
from django.core.management import call_command


class TestCreateCommand(TestCase):
    def test_invalid_command(self):
        args = ['blah']
        kwargs = {}
        with self.assertRaises(CommandError):
            call_command('pages', *args, **kwargs)

    def test_no_command(self):
        args = []
        kwargs = {}
        with self.assertRaises(CommandError):
            call_command('pages', *args, **kwargs)

    def test_pages_get_created(self):
        num_pages = len(Page.objects.all())
        args = ['create']
        kwargs = {'quantity': 1}
        call_command('pages', *args, **kwargs)
        self.assertEqual(len(Page.objects.all()), num_pages + 1)
