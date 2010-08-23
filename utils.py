from django.template.defaultfilters import slugify


def generate_unique_url(text, model, iteration=0):
    """Generate a unique url for a model from the provided text."""
    url = slugify(text)
    if iteration > 0:
        url = '%s-%s' %(iteration, url)
    url = '/%s' %(url[:49])
    try:
        print model.objects.get(url=url)
    except model.DoesNotExist:
        return url
    else:
        iteration += 1
        return generate_unique_url(text, model, iteration=iteration)

