from django.template.defaultfilters import slugify


def generate_unique_url(text, model, queryset=None, iteration=0):
    """Generate a unique url for a page from the provided text."""
    if queryset is None:
        queryset = model.objects
    slug = slugify(text)
    if iteration > 0:
        slug = '%s-%s' %(iteration, slug)
    url = '/%s' %(slug[:49])
    try:
        queryset.get(url=url)
    except model.DoesNotExist:
        return url
    else:
        iteration += 1
        return generate_unique_url(text, model, queryset=queryset,
            iteration=iteration)

