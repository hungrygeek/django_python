'''
Created on Mar 12, 2013

@author: giles
'''
from django import forms
from punts.models import Punt
from files.models import File
from members.models import Member

NAMEMAX = 200
SUMMARYMAX = 400
ORIGINMAX = 400
STATUSMAX = 200
PRIORLEN = 2
CATLEN   = 3

class TicketForm(forms.Form):
    PRIORCHOICES = (('MD', 'Medium'),
                    ('DA', 'Dangerous'),
                    ('IM', 'Immediate'),
                    ('HI', 'High'),
                    ('MD', 'Medium'),
                    ('LO', 'Low'))

    CATCHOICES = (('GEN', 'General'),
                  ('MAN', 'Maintenance'),
                  ('ORG', 'Organisation'),
                  ('MON', 'Money'),
                  ('WEB', 'Website'),
                  ('SOC', 'Social'),
                  ('COM', 'Committee'))
    
    #uid = models.BigIntegerField(primary_key=True)
    
    priority = forms.ChoiceField(choices=PRIORCHOICES)
    category = forms.ChoiceField(choices=CATCHOICES)
    summary  = forms.CharField(max_length=SUMMARYMAX)
    origin = forms.CharField(max_length = ORIGINMAX,required=False)
    status = forms.CharField(max_length = STATUSMAX,required=False)
    punts = forms.ModelMultipleChoiceField(queryset=Punt.objects.all(),required=False)
    files = forms.ModelMultipleChoiceField(queryset=File.objects.all(),required=False)
    autofiles = forms.CharField(widget=forms.HiddenInput,required=False)
    assignedto = forms.ModelMultipleChoiceField(queryset=Member.objects.all(),required=False)
    incoming = forms.CharField(widget=forms.Textarea,required=False)    
    outgoing = forms.CharField(widget=forms.Textarea,required=False)
    
