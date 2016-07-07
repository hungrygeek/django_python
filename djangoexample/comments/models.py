from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from comments.comment_utils import makeCF

# Create your models here.
class Comment(models.Model):    
    
    parent = generic.GenericForeignKey('content_type','content_id')
    
    submittedby = models.ForeignKey('members.Member')

    attachedfiles = models.ManyToManyField('files.File')
    
    content = models.TextField()

    submittedtime = models.DateTimeField()
    
    content_type = models.ForeignKey(ContentType)#,default= ContentType.objects.get(app_label="ticket", model="ticket"))
    
    content_id = models.PositiveIntegerField(null = True)

    subcomments = generic.GenericRelation('comments.Comment',content_type_field='content_type',
                               object_id_field='content_id')
    
    deleted = models.BooleanField(default=False)

    #subcomments = models.ManyToManyField('ticket.Comment')
    
    def get_overview_url(self):
        return '/comments/' + str(self.id) + '/'
    
    def get_sub_form(self):
        return makeCF(None,"comments", self.id)
    
    def get_parent_tag(self):
        return 'comments:' + str(self.id)