# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from thecut.core.admin import ModelAdmin
from thecut.pages.forms import PageAdminForm, SitesPageAdminForm
from thecut.pages.models import Page, SitesPage


class PageAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'headline', 'featured_content', 'content',
            'meta_description', 'tags']}),
        ('Publishing', {'fields': ['site', 'url',
            ('publish_at', 'is_enabled'), 'expire_at', 'publish_by',
            'template', 'is_featured', 'is_indexable',
            ('created_at', 'created_by'), ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = PageAdminForm
    list_display = ['title', 'publish_at', 'is_enabled', 'is_featured',
        'is_indexable']
    list_filter = ['publish_at', 'is_enabled', 'is_featured', 'is_indexable']
    prepopulated_fields = {'url': ['title']}
    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']
    search_fields = ['title']

admin.site.register(Page, PageAdmin)


class SitesPageAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'headline', 'featured_content', 'content',
            'meta_description', 'tags']}),
        ('Publishing', {'fields': ['sites', 'url',
            ('publish_at', 'is_enabled'), 'expire_at', 'publish_by',
            'template', 'is_featured', 'is_indexable',
            ('created_at', 'created_by'), ('updated_at', 'updated_by')],
            'classes': ['collapse']}),
    ]
    form = SitesPageAdminForm
    list_display = ['title', 'publish_at', 'is_enabled', 'is_featured',
        'is_indexable']
    list_filter = ['publish_at', 'is_enabled', 'is_featured', 'is_indexable']
    prepopulated_fields = {'url': ['title']}
    readonly_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']
    search_fields = ['title']

admin.site.register(SitesPage, SitesPageAdmin)

