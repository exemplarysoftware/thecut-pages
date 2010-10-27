from datetime import datetime
from django import forms
from django.contrib.sites.models import Site
from pages.models import Page, SitesPage


class PageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        self.fields['publish_at'].initial = datetime.now()
        self.fields['site'].initial = Site.objects.get_current()
    
    class Meta:
        model = Page


class SitesPageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SitesPageAdminForm, self).__init__(*args, **kwargs)
        self.fields['publish_at'].initial = datetime.now()
        self.fields['sites'].initial = [Site.objects.get_current()]
    
    class Meta:
        model = SitesPage

