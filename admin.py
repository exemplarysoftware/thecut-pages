from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline
from pages.forms import PageAdminForm, SitesPageAdminForm
from pages.models import Page, SitesPage


PAGE_INLINES = []

if 'media' in settings.INSTALLED_APPS:
    try:
        from media.admin import MediaSetInline
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


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'headline', 'content',
            'meta_description', 'tags']}),
        ('Publishing', {'fields': ['site', 'url',
            ('publish_at', 'is_enabled'), 'publish_by', 'template',
            'is_featured', 'is_indexable'], 'classes': ['collapse']}),
    ]
    form = PageAdminForm
    inlines = PAGE_INLINES
    list_display = ['title', 'publish_at', 'is_enabled',
        'is_featured', 'is_indexable']
    list_filter = ['publish_at', 'is_enabled', 'is_featured',
        'is_indexable']
    prepopulated_fields = {'url': ['title']}
    search_fields = ['title']
    
    def save_model(self, request, obj, form, change):
        if not change: obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

admin.site.register(Page, PageAdmin)


class SitesPageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'headline', 'content',
            'meta_description', 'tags']}),
        ('Publishing', {'fields': ['sites', 'url',
            ('publish_at', 'is_enabled'), 'publish_by', 'template',
            'is_featured', 'is_indexable'], 'classes': ['collapse']}),
    ]
    form = SitesPageAdminForm
    inlines = PAGE_INLINES
    list_display = ['title', 'publish_at', 'is_enabled',
        'is_featured', 'is_indexable']
    list_filter = ['publish_at', 'is_enabled', 'is_featured',
        'is_indexable']
    prepopulated_fields = {'url': ['title']}
    search_fields = ['title']
    
    def save_model(self, request, obj, form, change):
        if not change: obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

admin.site.register(SitesPage, SitesPageAdmin)

