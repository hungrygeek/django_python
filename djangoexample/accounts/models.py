from django.db import models
from members.models import Member

# Create your models here.

ACCOUNTLEN=100

class AccountItem(models.Model):
    
    uid = models.BigIntegerField(primary_key=True)
    
    createdby = models.ForeignKey('members.Member')

    attachedfiles = models.ManyToManyField('files.File')
    
    notes = models.TextField()

    submittedtime = models.DateTimeField()

    ticket = models.ForeignKey('ticket.Ticket')

    comments = models.ManyToManyField('comments.Comment')

    transactionwith = models.TextField()

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    account = models.CharField(max_length=ACCOUNTLEN)

    balancewhendrawn = models.DecimalField(max_digits=10, decimal_places=2)