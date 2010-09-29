from django.db.models import Manager


class QuerySetManager(Manager):
    # http://djangosnippets.org/snippets/734/
    def get_query_set(self):
        return self.model.QuerySet(self.model)
    def __getattr__(self, attr, *args):
        return getattr(self.get_query_set(), attr, *args)

