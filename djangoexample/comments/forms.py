'''
Created on 27 Mar 2013

@author: giles
'''
from django import forms
from punts.models import Punt
from files.models import File
from members.models import Member

class CommentForm(forms.Form):
    parent = forms.CharField(widget=forms.HiddenInput, required=True)
    content = forms.CharField(widget=forms.Textarea,required=True)
    files = forms.ModelMultipleChoiceField(queryset=File.objects.all(),required=False)
    autofiles = forms.CharField(widget=forms.HiddenInput,required=False)
    suid    = forms.CharField(widget=forms.HiddenInput,required=True)