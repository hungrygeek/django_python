'''
Created on Mar 18, 2013

@author: giles
'''
from django.http import HttpResponse, HttpResponseRedirect
from comments.models import Comment
from comments.forms import CommentForm
from ticket.models import Ticket
from django.contrib.contenttypes.models import ContentType
from files.fileutils import getfilesfromfields
import datetime
from general.suid_store import suidStore
from sjcpunts.views import nopage_err

suid_store = suidStore()


def add(request):
    print "Hit add request for comment"
    r = '/'
    if request.method =='POST':
        form = CommentForm(request.POST)
        #print repr(form.cleaned_data)
        #print request.POST
        if form.is_valid():
            d = form.cleaned_data
            #print d['suid']
            if suid_store.check(d['suid']):
                suid_store.add(d['suid'])
                suid_store.trim()
                c = Comment()
                p = d['parent'].split(':')
                pt = Ticket
                r = '/tickets/'
                print p[0]
                if p[0] in ('ticket','Ticket'):
                    pt = Ticket
                    r = '/tickets/'
                elif p[0] in ('comment','com','Comment','comments','Comments'):
                    pt = Comment
                    r = '/comments/'
                #print r
                #Insert other comment parents here
                try:
                    p = pt.objects.get(id=int(p[1]))
                    #print "Got model of type " + str(type(pt))
                    r += str(p.id) + '/'
                except:
                    #print 'Cannot get model of type ' + str(type(pt))
                    return HttpResponse('Invalid Parent')
                #c.content_type = ContentType.objects.get_for_model(pt)
                c.parent = p
                c.submittedby = request.user.member
                c.submittedtime = datetime.datetime.now()
                c.content = d['content']

                c.save()
                #print d['files']
                fs = getfilesfromfields(d['files'],d['autofiles'])
                if fs:
                    print fs
                    c.attachedfiles.add(*fs)
                c.save()
                
                #print "Id for new comment", c.id
                #print r
            else:
                print "Suid seen before"
        else:
            print "Form is invalid"
        #print r
        return HttpResponseRedirect(r)
                
def parent(request, comment_id):
    try:
        c = Comment.objects.get(id=comment_id)
        cp = c.parent.get_overview_url()
        return HttpResponseRedirect(cp)
    except:
        pass
    return nopage_err(request,"Comment does not exist")