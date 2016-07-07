from django.db import models

# Create your models here.

NAMEMAX = 200
EMAILMAX = 200
STATUSMAX = 200

class Punt(models.Model):
    # Name is stored First Last
    name = models.CharField(max_length = NAMEMAX)
    # Number of the punt
    number = models.IntegerField()
    # status is stored by a set of keywords
    status = models.CharField(max_length = STATUSMAX)
    # Time the punt joined the society
    purchasedate = models.DateField()
    # Notes on a user
    notes = models.TextField()
    # maintenance history
    maintenance = models.ManyToManyField('ticket.Ticket')
    
    files = models.ManyToManyField('files.File')
    
    def __unicode__(self):
        return str(self.number) + ' : ' + self.name
    
    def get_overview_url(self):
        return '/punts/' + self.id + '/'