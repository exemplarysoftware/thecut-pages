from django.template.defaultfilters import slugify


def generate_unique_slug(text, model, queryset=None, iteration=0):
    """Generate a unique slug for a model from the provided text."""
    if queryset is None:
        queryset = model.objects
    slug = slugify(text)
    if iteration > 0:
        slug = '%s-%s' %(iteration, slug)
    slug = slug[:50]
    try:
        print queryset.get(slug=slug)
    except model.DoesNotExist:
        return slug
    else:
        iteration += 1
        return generate_unique_slug(text, model, queryset=queryset,
            iteration=iteration)

