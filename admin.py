from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline, GenericTabularInline
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
    date_hierarchy = 'publish_at'
    inlines = PAGE_INLINES
    list_display = ['title', 'url', 'publish_at', 'is_enabled', 'site']
    list_filter = ['site']
    prepopulated_fields = {'url': ['title']}
    search_fields = ['title', 'headline', 'url']
    
    def save_model(self, request, obj, form, change):
        if not change: obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

admin.site.register(Page, PageAdmin)


class SitesPageAdmin(admin.ModelAdmin):
    date_hierarchy = 'publish_at'
    inlines = PAGE_INLINES
    list_display = ['title', 'url', 'publish_at', 'is_enabled']
    list_filter = ['sites']
    prepopulated_fields = {'url': ['title']}
    search_fields = ['title', 'headline', 'url']
    
    def save_model(self, request, obj, form, change):
        if not change: obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

admin.site.register(SitesPage, SitesPageAdmin)

