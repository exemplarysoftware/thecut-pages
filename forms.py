from datetime import datetime
from django import forms
from pages.models import Page
#from photologue.models import Photo, Document
#from video.models import Video
#from widgets.widgets import AjaxImageWidget, AjaxDocumentWidget, AjaxVideoWidget


class PageForm(forms.ModelForm):
    #photos = forms.ModelMultipleChoiceField(widget=AjaxImageWidget(options={'help':'Pick images'}), queryset=Photo.objects.filter(is_public=True), required=False)
    #documents = forms.ModelMultipleChoiceField(widget=AjaxDocumentWidget(options={'help':'Pick documents'}), queryset=Document.objects.filter(is_public=True), required=False)    
    #videos = forms.ModelMultipleChoiceField(widget=AjaxVideoWidget(options={'help':'Pick videos'}), queryset=Video.objects.filter(is_public=True), required=False)        
    
    publish_at = forms.DateTimeField(label='Publish Date & Time',
        widget=forms.DateTimeInput(format='%d/%m/%Y %I:%M %p'),
        input_formats=['%d/%m/%Y %I:%M %p', '%d/%m/%Y %H:%M', '%d/%m/%y %I:%M %p', '%d/%m/%y %H:%M'],
        initial=datetime.now(),
        help_text='Page will only be viewable on the website once this date and time has past.')
    
    class Meta:
        fields = ['title', 'headline', 'content',
            'publish_at', 'is_public', 'site']
        model = Page

