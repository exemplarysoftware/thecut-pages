# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify


def generate_unique_url(text, queryset, url_field='url', iteration=0):
    """Generate a unique url for a model from the provided text."""
    slug = slugify(text)

    if iteration > 0:
        slug = '{0}-{1}'.format(iteration, slug)
    url = '/{0}'.format(slug[:99])

    try:
        queryset.get(**{url_field: url})
    except ObjectDoesNotExist:
        return url
    else:
        iteration += 1
        return generate_unique_url(text, queryset=queryset,
                                   url_field=url_field, iteration=iteration)
