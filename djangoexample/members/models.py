from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

NAMEMAX = 200
EMAILMAX = 200
STATUSMAX = 200

class Member(models.Model):
    user = models.OneToOneField(User)
    # status is stored by a set of keywords
    status = models.CharField(max_length = STATUSMAX,blank=True)
    # Time the user joined the society
    joindate = models.DateField(default=datetime.now)
    # Notes on a user
    notes = models.TextField(blank=True)
    # Bio
    bio = models.TextField(blank=True)
    # User files
    files = models.ManyToManyField('files.File',blank=True)
    
    def __unicode__(self):
        name = self.user.username
        if self.user.first_name:
            name = self.user.first_name
        return name + " (" + self.user.email + ")"
    
    def short_name(self):
        name = self.user.username
        if self.user.first_name:
            name = self.user.first_name
        return name

    def get_overview_url(self):
        #print "Member.get_overview_url called"
        return '/users/' + self.user.username + '/'