from django.db import models


import fileutils

# Create your models here.

# Create your models here.
NAMEMAX = 200
SUMMARYMAX = 400
ORIGINMAX = 400
STATUSMAX = 200
PRIORLEN = 2
CATLEN   = 3

NOICON = 0
DFICON = 1
EXICON = 2 # The iconlink points to the icon
CUICON = 3 # The iconfile points to the icon

class File(models.Model):
    
    #uid = models.BigIntegerField(primary_key=True)
    
    name      = models.CharField(max_length=NAMEMAX)
    
    tags       = models.TextField(blank=True)
    
    easyname   = models.CharField(max_length=NAMEMAX,blank=True)
    
    createdby  = models.ForeignKey('members.Member')
    
    actualfile = models.FileField(upload_to="userfiles")
    
    # see fileutils
    iconsource = models.IntegerField(null = False, default=(NOICON))
    
    iconlink   = models.ForeignKey('files.Icon',null = True,related_name="relfiles")
    
    iconfile   = models.FileField(upload_to=fileutils.userfile_icon_root, null = True)
    
    deleted = models.BooleanField(default=False)
    
    lasttouched = models.DateTimeField()
    
    
    def __unicode__(self):
        return self.easyname + ' (' + self.createdby.short_name() + ')';
    
    def get_icon_url(self):
        if self.iconsource == fileutils.CUICON:
            return self.iconfile.url
        elif self.iconsource == fileutils.EXICON:
            return self.iconlink.file.url
        else:
            return fileutils.dficonurl
    
class Icon(models.Model):
    name      = models.CharField(max_length=NAMEMAX)
    filetypes = models.CharField(max_length=NAMEMAX)
    file      = models.FileField(upload_to="icons")