from django.views.decorators.csrf import csrf_protect
from django.views.generic.list_detail import object_detail
from thecut.pages.models import Page, SitesPage


@csrf_protect
def page(request, url):
    """Wrapper for page_detail view."""
    return page_detail(request, url)


def page_detail(request, url, queryset=None, **kwargs):
    kwdefaults = {'slug': url, 'slug_field': 'url',
        'template_name_field': 'template',
        'template_object_name': 'page'}
    
    for key, value in kwdefaults.items():
        if not key in kwargs:
            kwargs.update({key: value})
    
    if not queryset:
        queryset = Page.objects.current_site().active().filter(url=url) \
            or SitesPage.objects.current_site().active().filter(url=url)
    
    return object_detail(request, queryset, **kwargs)

