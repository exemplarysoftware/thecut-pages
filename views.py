from django.conf import settings
from django.contrib.sites.models import Site
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list
from pages.forms import PageForm
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
    site = Site.objects.get_current()
    page = get_object_or_404(Page.objects.active(), url=url, site=site)
    context = extra_context is not None and extra_context or {}
    context.update({'page': page})
    
    # Set template, if one is stored.
    template = page.template and page.template or DEFAULT_TEMPLATE
    
    return render_to_response(template, context,
        context_instance=RequestContext(request))


def pages(request):
    """Wrapper for page_list view."""
    return page_list(request)

def page_list(request):
    """List pages."""
    pages = Page.objects.all()
    return object_list(request, queryset=pages,
        template_object_name='page',
        template_name='pages/page_list.html')


def page_edit(request, pk, template='pages/page_edit.html',
    redirect_to=None):
    """Edit/update page."""
    page = get_object_or_404(Page, pk=pk)
    if request.method == "POST":
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            if request.is_ajax():
                return HttpResponse(serialize('json', [page]),
                    mimetype='text/plain')
            else:
                return redirect(redirect_to)
    else:
        form = PageForm(instance=page)
    if request.is_ajax():
        return HttpResponseBadRequest('error', mimetype='text/plain')
    else:
        return render_to_response(template,
            {'page': page, 'form': form},
            context_instance=RequestContext(request))

