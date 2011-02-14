from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline
from thecut.core.admin import ModelAdmin
from thecut.pages.forms import PageAdminForm, SitesPageAdminForm
from thecut.pages.models import Page, SitesPage


PAGE_INLINES = []

if 'thecut.media' in settings.INSTALLED_APPS:
    try:
        from thecut.media.admin import MediaSetInline
    except ImportError:
        pass
    else:
        PAGE_INLINES += [MediaSetInline]


if 'ctas' in settings.INSTALLED_APPS:
    try:
        from ctas.models import AttachedCallToAction
    except ImportError:
        pass
    else:
        class PageCallToActionInline(GenericTabularInline):
            extra = 1
            model = AttachedCallToAction
        
        PAGE_INLINES += [PageCallToActionInline]


class PageAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'headline', 'content',
            'meta_description', 'tags']}),
        ('Publishing', {'fields': ['site', 'url',
            ('publish_at', 'is_enabled'), 'expire_at', 'publish_by',
            'template', 'is_featured', 'is_indexable'],
            'classes': ['collapse']}),
    ]
    form = PageAdminForm
    inlines = PAGE_INLINES
    list_display = ['title', 'publish_at', 'is_enabled',
        'is_featured', 'is_indexable']
    list_filter = ['publish_at', 'is_enabled', 'is_featured',
        'is_indexable']
    prepopulated_fields = {'url': ['title']}
    search_fields = ['title']

admin.site.register(Page, PageAdmin)


class SitesPageAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'headline', 'content',
            'meta_description', 'tags']}),
        ('Publishing', {'fields': ['sites', 'url',
            ('publish_at', 'is_enabled'), 'expire_at', 'publish_by',
            'template', 'is_featured', 'is_indexable'],
            'classes': ['collapse']}),
    ]
    form = SitesPageAdminForm
    inlines = PAGE_INLINES
    list_display = ['title', 'publish_at', 'is_enabled',
        'is_featured', 'is_indexable']
    list_filter = ['publish_at', 'is_enabled', 'is_featured',
        'is_indexable']
    prepopulated_fields = {'url': ['title']}
    search_fields = ['title']

admin.site.register(SitesPage, SitesPageAdmin)

