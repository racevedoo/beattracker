# -*- coding: utf-8 -*-
from django import forms

class UploadTrackForm(forms.Form):
    track_file = forms.FileField(
        label='Select a file',
        help_text='Select a wav file'
    )