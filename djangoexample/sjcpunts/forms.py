'''
Created on 25 Mar 2013

@author: giles
'''
from django import forms


NAMEMAX = 200
SUMMARYMAX = 400
ORIGINMAX = 400
STATUSMAX = 200
PRIORLEN = 2
CATLEN   = 3

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)