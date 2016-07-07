from django.db import models

NAMEMAX = 200

class File(models.Model):
    
    uid = models.BigIntegerField(primary_key=True)
    
    name = models.CharField(max_length=NAMEMAX)
    
    createdby = models.ForeignKey(Member)
    
    actualfile = models.FileField(upload_to="userfiles")

    
