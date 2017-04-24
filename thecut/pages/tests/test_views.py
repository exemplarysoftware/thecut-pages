# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from thecut.pages.factories import PageFactory
from thecut.pages.views import page as page_view
from django.test.client import RequestFactory


# From http://stackoverflow.com/a/27203814
def setup_view(view, request, *args, **kwargs):
    """Mimic as_view() returned callable, but returns view instance.

    args and kwargs are the same you would pass to ``reverse()``

    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view


class TestDetailView(TestCase):
    def test_getting_page(self):
        PageFactory(title='Hello world', url='/hello')

        #request_factory = RequestFactory()
        #request = request_factory.get('/hello')
        #response = page_view(request, '/hello')
        #self.assertEqual(response.context_data['page'].title, 'Hello world')

        request_factory = RequestFactory()
        request = request_factory.get('hello')
        response = page_view(request, 'hello')
        self.assertEqual(response.context_data['page'].title, 'Hello world')
