from django.http import HttpResponse, HttpResponseRedirect
from django.template import  loader, RequestContext
from django.contrib.auth.decorators import login_required
from punts.models import Punt

@login_required(login_url='/login/')
def detail(request,punt_id):
    punt = None
    message = ""
    isme = False
    try:
        tpunt = Punt.objects.get(id=punt_id)
    
        if tpunt is not None:
            punt = tpunt
    except:
        message = "Punt not found"
    args = {'punt':punt,'message':message}
    c = RequestContext(request,args)
    t = loader.get_template('punts/individual.html')
    return HttpResponse(t.render(c))


@login_required(login_url='/login/')
def index(request):
    punts = Punt.objects.all()
    args = {'punts':punts}
    c = RequestContext(request,args)
    t = loader.get_template('punts/index.html')
    return HttpResponse(t.render(c))