from django.conf import settings
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from pages.models import Page


try:
    from django.views.decorators.csrf import csrf_protect
except ImportError:
    def csrf_protect(obj):
        return obj


DEFAULT_TEMPLATE = getattr(settings, 'PAGES_DEFAULT_TEMPLATE',
    'pages/page_detail.html')


@csrf_protect
def page(request, url):
    """Wrapper for page_detail view."""
    return page_detail(request, url)

def page_detail(request, url, extra_context=None):
    page = get_object_or_404(Page.objects.current_site().active(),
        url=url, site=site)
    context = extra_context or {}
    context.update({'page': page})
    
    # Set template, if one is stored.
    template = page.template and page.template or DEFAULT_TEMPLATE
    
    return render_to_response(template, context,
        context_instance=RequestContext(request))

