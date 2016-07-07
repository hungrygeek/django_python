'''
Created on Mar 18, 2013

@author: giles
'''
from django.http import HttpResponse, HttpResponseRedirect
from ticket.models import Comment
from ticket.forms import CommentForm
from ticket.models import Ticket
from django.contrib.contenttypes.models import ContentType
from fileutils import getfilesfromfields
import datetime


def add(request):
    r = '/'
    if request.method =='POST':
        form = CommentForm(request.POST)
        #print repr(form.cleaned_data)
        print request.POST
        if form.is_valid():
            d = form.cleaned_data
            c = Comment()
            p = d['parent'].split(':')
            pt = Ticket
            r = '/ticket/'
            if p[0] in ('ticket','Ticket'):
                pt = Ticket
                r = '/tickets/'
            print r
            #Insert other comment parents here
            try:
                p = pt.objects.get(id=int(p[1]))
                print "Got model of type " + str(type(pt))
                r += str(p.id) + '/'
            except:
                print 'Cannot get model of type ' + str(type(pt))
                return HttpResponse('Invalid Parent')
            #c.content_type = ContentType.objects.get_for_model(pt)
            c.parent = p
            c.submittedby = request.user.member
            c.submittedtime = datetime.datetime.now()
            c.content = d['content']
            c.save()
            fs = getfilesfromfields(d['files'],d['autofiles'])
            if fs:
                c.attachedfiles.add(*fs)
            c.save()
            print r
        else:
            print "Form is invalid"
        print r
        return HttpResponseRedirect(r)
                