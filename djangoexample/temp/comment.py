from django.db import models
from members.models import Member
from tickets.models import Ticket
from files.models import File

# Create your models here.

class Comment(models.Model):
    
    uid = models.BigIntegerField(primary_key=True)
    
    submittedby = models.ForeignKey(Member)

    attachedfiles = models.ManyToManyField(File)
    
    content = models.TextField()

    submittedtime = models.DateTimeField()

    ticket = models.ForeignKey(Ticket)

    subcomments = models.ManyToManyField(Comment)
