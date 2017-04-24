# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase, override_settings
from thecut.pages.middleware import PageMiddleware
from thecut.pages.factories import PageFactory
from django.test.client import RequestFactory
from mock import MagicMock, patch
from django.template.response import TemplateResponse


class TestMiddleware(TestCase):
    def test_normal_operation(self):
        PageFactory(title='Hello world', url='/hello')

        m = PageMiddleware()
        request_factory = RequestFactory()
        request = request_factory.get('/hello')

        response = MagicMock()
        response.status_code = 404

        response2 = m.process_response(request, response)

        self.assertEqual(response2.context_data['page'].title, 'Hello world')

    def test_normal_operation_unknown_page(self):
        PageFactory(title='Hello world', url='/hello')

        m = PageMiddleware()
        request_factory = RequestFactory()
        request = request_factory.get('/hello2')

        response = MagicMock()
        response.status_code = 404

        response2 = m.process_response(request, response)

        self.assertIs(response, response2)

    def test_url_already_used(self):
        PageFactory(title='Hello world', url='/hello')

        m = PageMiddleware()
        request_factory = RequestFactory()
        request = request_factory.get('/hello')

        response = MagicMock()
        response.status_code = 200

        response2 = m.process_response(request, response)

        self.assertIs(response, response2)

    @patch.object(TemplateResponse, 'render')
    def test_render_is_called(self, mock_render):
        PageFactory(title='Hello world', url='/hello')

        m = PageMiddleware()
        request_factory = RequestFactory()
        request = request_factory.get('/hello')

        response = MagicMock()
        response.status_code = 404

        m.process_response(request, response)

        mock_render.assert_called_once_with()

    @override_settings(DEBUG=False)
    @patch('thecut.pages.middleware.page')
    def test_normal_operation_non_404_error(self, mock_page):
        PageFactory(title='Hello world', url='/hello')

        m = PageMiddleware()
        request_factory = RequestFactory()
        request = request_factory.get('/hello')

        response = MagicMock()
        response.status_code = 404

        mock_page.side_effect = Exception()

        response2 = m.process_response(request, response)

        self.assertEqual(mock_page.call_count, 1)

        self.assertIs(response, response2)

    @override_settings(DEBUG=True)
    @patch('thecut.pages.middleware.page')
    def test_normal_operation_non_404_error_debug_mode(self, mock_page):
        PageFactory(title='Hello world', url='/hello')

        m = PageMiddleware()
        request_factory = RequestFactory()
        request = request_factory.get('/hello')

        response = MagicMock()
        response.status_code = 404

        mock_page.side_effect = Exception()

        with self.assertRaises(Exception):
            m.process_response(request, response)

        self.assertEqual(mock_page.call_count, 1)

    @patch.object(TemplateResponse, 'render')
    @patch('thecut.pages.middleware.page')
    def test_normal_operation_no_render_function(self, mock_page, mock_render):
        PageFactory(title='Hello world', url='/hello')

        m = PageMiddleware()
        request_factory = RequestFactory()
        request = request_factory.get('/hello')

        response = MagicMock()
        response.status_code = 404

        mock_page.return_value = 1

        m.process_response(request, response)

        self.assertEqual(mock_render.call_count, 0)
