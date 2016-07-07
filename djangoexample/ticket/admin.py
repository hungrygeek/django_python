'''
Created on Mar 7, 2013

@author: giles
'''
from django.contrib import admin
from ticket.models import Ticket
from comments.models import Comment

admin.site.register(Ticket)
admin.site.register(Comment)
