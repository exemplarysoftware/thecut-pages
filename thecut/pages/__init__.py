from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('thecut.pages.views',
    url(r'^(?P<url>[\w/-]+)$', 'page_detail', name='page_detail'),
)

urls = (urlpatterns, 'pages', 'pages')

