# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from thecut.pages.management.commands.pages import Command
from django.core.management.base import CommandError
import io
from thecut.pages.models import Page


class TestCreateCommand(TestCase):
    def test_invalid_command(self):
        c = Command()
        out = io.StringIO()
        with self.assertRaises(CommandError):
            c.handle('blah', quantity=1, stdout=out)
        self.assertEqual(out.getvalue(), '')

    def test_pages_get_created(self):
        num_pages = len(Page.objects.all())
        c = Command()
        out = io.StringIO()
        c.handle('create', quantity=1, stdout=out)
        self.assertEqual(len(Page.objects.all()), num_pages + 1)

