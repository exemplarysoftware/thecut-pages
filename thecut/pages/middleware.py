# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from django.http import Http404
from thecut.pages.views import page


class PageMiddleware(object):
    # Adapted from the Django FlatpageFallbackMiddleware

    def process_response(self, request, response):
        if response.status_code != 404:
            return response  # No need to check for a page on non-404 responses
        try:
            response = page(request, request.path_info)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response
        else:
            if hasattr(response, 'render') and callable(response.render):
                response.render()
            return response
