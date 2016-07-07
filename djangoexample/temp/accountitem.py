from django.db import models
from members.models import Member
from tickets.models import Ticket
from files.models import File

# Create your models here.

ACCOUNTLEN=100

class AccountItem(models.Model):
    
    uid = models.BigIntegerField(primary_key=True)
    
    filedby = models.ForeignKey(Member)

    attachedfiles = models.ManyToManyField(File)
    
    notes = models.TextField()

    submittedtime = models.DateTimeField()

    ticket = models.ForeignKey(Ticket)

    comments = models.ManyToManyField(Comment)

    transactionwith = models.TextField()

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    account = models.CharField(max_length=ACCOUNTLEN)

    balancewhendrawn = models.DecimalField(max_digits=10, decimal_places=2)
