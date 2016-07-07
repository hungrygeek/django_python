# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext
from ticket.models import Ticket
from files.models import File
from ticket.forms import TicketForm
from comments.forms import CommentForm
import datetime
from django.contrib.auth.decorators import login_required
from comments.comment_utils import makeCF,generateView
from sjcpunts.views import permission_err



@login_required(login_url='/login/')
def index(request):
    ticket_list = Ticket.objects.exclude(deleted=True).order_by('-filedtime')
    args = {'ticket_list':ticket_list,
            'string_ticket_ordering':"Time Filed"}
    c = RequestContext(request,args)
    t = loader.get_template('ticket/index.html')
    return HttpResponse(t.render(c))

@login_required(login_url='/login/')
def detail(request, ticket_id):
    cpairs = []
    try:
        message = ""
        ticket = Ticket.objects.get(pk=ticket_id)
        ticket.lasttouched = datetime.datetime.now()
        ticket.save()
        for c in ticket.comments.all():
            cpairs.append((c,makeCF(request.user, "ticket", ticket_id)))
        cgen = generateView(ticket.comments.all(),request,can_comment=True)
    except Ticket.DoesNotExist:
        message = "Ticket does not exist"
        ticket = None
    cf = makeCF(request.user, "ticket", ticket_id)
    
    args = {'ticket':ticket,'message':message,'commentform':cf,'cpairs':cpairs,'cgen':cgen}
    #print len(ticket.comments.all())
    args['filecols'] = 5
    c = RequestContext(request,args)
    t = loader.get_template('ticket/individual.html')
    return HttpResponse(t.render(c))

def newticket(request, form = TicketForm()):
    args = {'form': form}
    c = RequestContext(request,args)
    t = loader.get_template('ticket/addnew.html')
    return HttpResponse(t.render(c))


@login_required(login_url='/login/')
def add(request):
    if request.method =='POST':
        form = TicketForm(request.POST)
        #print repr(form.cleaned_data)
        print request.POST
        if form.is_valid():
            d = form.cleaned_data
            t = Ticket()
            t.priority = d['priority']
            t.category = d['category']
            t.summary = d['summary']
            t.filedtime = datetime.datetime.now()
            t.lasttouched = t.filedtime
            t.filedby = request.user.member
            t.origin = d['origin']
            t.status = d['status']
            t.save()
            t.punts = d['punts']
            fs = d['autofiles']
            fs = fs.split(',')
            for f in fs:
                try:
                    f = int(f)
                    af = File.objects.get(id=f)
                    t.files.add(af)
                except:
                    pass
                    
            
            t.files.add(*d['files'])
            t.assignedto.add(*d['assignedto'])
            t.save()
            #print repr(form.cleaned_data)
            return HttpResponseRedirect(('/tickets/'+str(t.id)+'/'))
            return detail(request, t.id)
    else:
        form = TicketForm()
    return newticket(request,form)

def delete(request,ticket_id):
    try:
        message = ""
        ticket = Ticket.objects.get(pk=ticket_id)
        ticket.lasttouched = datetime.datetime.now()
        if request.user.has_perm('ticket.can_fake_delete'):
            ticket.deleted = True
            if request.user.has_perm('ticket.can_real_delete'):
                args = {'message':("Do you really want to delete ticket: '" + ticket.summary +"'?")}
                c = RequestContext(request,args)
                t = loader.get_template('ticket/reallydelete.html')
                return HttpResponse(t.render(c))
        else:
            return permission_err(request, message="Only a member can delete a ticket")
        ticket.save()
    except Ticket.DoesNotExist:
        message = "Ticket does not exist"
        ticket = None
    return HttpResponseRedirect(('/tickets/'))

def delete_real(request,ticket_id):
    try:
        message = ""
        ticket = Ticket.objects.get(pk=ticket_id)
        ticket.lasttouched = datetime.datetime.now()
        if request.user.has_perm('ticket.can_real_delete'):
            ticket.delete()
        else:
            return permission_err(request, message="Only a committee member can delete a ticket perminantly")
    except Ticket.DoesNotExist:
        message = "Ticket does not exist"
        ticket = None
    return HttpResponseRedirect(('/tickets/'))
    
    
def delete_fake(request,ticket_id):
    try:
        message = ""
        ticket = Ticket.objects.get(pk=ticket_id)
        ticket.lasttouched = datetime.datetime.now()
        if request.user.has_perm('ticket.can_fake_delete'):
            ticket.deleted = True
        else:
            return permission_err(request, message="Only a member can delete a ticket")
        ticket.save()
    except Ticket.DoesNotExist:
        message = "Ticket does not exist"
        ticket = None
    return HttpResponseRedirect(('/tickets/'))