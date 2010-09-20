from django.conf import settings


def attach_mediaset(obj):
    obj.media = None
    return obj
if 'media' in settings.INSTALLED_APPS:
    try:
        from media.decorators import attach_mediaset
    except ImportError:
        pass

