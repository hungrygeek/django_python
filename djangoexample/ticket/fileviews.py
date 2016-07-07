'''
Created on Mar 13, 2013

@author: giles
'''
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext
from django.utils import simplejson
from ticket.models import File
from django.views.decorators.csrf import csrf_exempt
import tempfile
import general.chartimestamp as cts
import time
import datetime

@csrf_exempt
def add(request):
    if not request.method=='POST':
        print repr(request.method)
        return HttpResponseRedirect('/')
    xhr = request.GET.has_key('xhr')
    response_dict = {}
    response_dict.update({'success': True})
    for f in request.FILES.getlist('file'):
        #print type(f)
        with tempfile.NamedTemporaryFile() as tmp:
            for chunk in f.chunks():
                tmp.write(chunk)
            tmp.seek(0)
            
            #print type(request.user)
            #print repr(request.user.member)
            name = str(request.user.username) + '_' + cts.build_timestamp(time.time()) + '_' + f.name
            mfile = File(name=name, easyname=f.name,createdby=request.user.member,lasttouched=datetime.datetime.now())
            mfile.actualfile.save(name,f,save=False)
            mfile.save()
            response_dict.update({'uid':str(mfile.id)})
        tmp.close()
        #print name
            
    #print repr(request.FILES)
    
    return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    return HttpResponseRedirect('/')
