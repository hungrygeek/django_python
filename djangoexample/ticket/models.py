from django.db import models

import files.fileutils
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

# Create your models here.
NAMEMAX = 200
SUMMARYMAX = 400
ORIGINMAX = 400
STATUSMAX = 200
PRIORLEN = 2
CATLEN   = 3

class Ticket(models.Model):
    PRIORCHOICES = (('DA', 'Dangerous'),
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

    priority = models.CharField(max_length=PRIORLEN,choices=PRIORCHOICES, default='MD')

    category = models.CharField(max_length=CATLEN,choices=CATCHOICES, default='GEN')
    
    summary = models.CharField(max_length=SUMMARYMAX)

    filedtime = models.DateTimeField()
    
    filedby = models.ForeignKey('members.Member')
    
    origin = models.CharField(max_length = ORIGINMAX,blank=True)
    
    status = models.CharField(max_length = STATUSMAX,blank=True)
    
    punts = models.ManyToManyField('punts.Punt', null=True,blank=True)

    files = models.ManyToManyField('files.File',null=True,blank=True)
    
    assignedto = models.ManyToManyField('members.Member', related_name="tickets_assigned", null=True,blank=True)
    
    incoming = models.TextField(blank=True)
    
    outgoing = models.TextField(blank=True)

    #comments = models.ManyToManyField(Comment,null=True,blank=True)
    
    comments = generic.GenericRelation('comments.Comment',content_type_field='content_type', object_id_field='content_id')

    deleted = models.BooleanField(default=False)
    
    lasttouched = models.DateTimeField()

    def get_overview_url(self):
        return '/tickets/' + str(self.id) + '/'
