from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericStackedInline, GenericTabularInline
from django.forms import ModelForm
from pages.models import Page


PAGE_INLINES = []

if 'media' in settings.INSTALLED_APPS:
    try:
        from media.fields import ImageMultipleChoiceField
        from media.models import MediaSet
        from photologue.models import Photo
    except ImportError:
        pass
    else:
        class MediaSetForm(ModelForm):
            photos = ImageMultipleChoiceField(Photo.objects.all(),
                required=False)
            class Meta:
                model = MediaSet
        
        class PageMediaInline(GenericStackedInline):
            extra = 1
            filter_horizontal = ['photos', 'galleries', 'documents']
            form = MediaSetForm
            max_num = 1
            model = MediaSet
        
        PAGE_INLINES += [PageMediaInline]


if 'ctas' in settings.INSTALLED_APPS:
    try:
        from ctas.models import AttachedCallToAction
    except ImportError:
        pass
    else:
        class PageCallToActionInline(GenericTabularInline):
            extra = 1
            max_num = 1
            model = AttachedCallToAction
            exclude = ['order']
        
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
