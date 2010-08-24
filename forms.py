from datetime import datetime
from django import forms
from pages.models import Page


class PageForm(forms.ModelForm):
    publish_at = forms.DateTimeField(label='Publish Date & Time',
        widget=forms.DateTimeInput(format='%d/%m/%Y %I:%M %p'),
        input_formats=['%d/%m/%Y %I:%M %p', '%d/%m/%Y %H:%M', '%d/%m/%y %I:%M %p', '%d/%m/%y %H:%M'],
        initial=datetime.now(),
        help_text='Page will only be viewable on the website once this date and time has past.')
    
    class Meta:
        fields = ['title', 'headline', 'content',
            'publish_at', 'is_public', 'site']
        model = Page

