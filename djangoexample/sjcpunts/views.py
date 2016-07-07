'''
Created on Mar 12, 2013

@author: giles
'''
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader, RequestContext
from sjcpunts.forms import LoginForm
from django.contrib.auth import authenticate, login,logout
#TODO Add a home page view for logged in users
def index(request):
    c = RequestContext(request,{'test':"Test"})
    t = loader.get_template('sjcpunts/index.html')
    return HttpResponse(t.render(c))
#TODO Finish the login
def mylogin(request):
    message = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            un = d['username']
            ps = d['password']
            user = authenticate(username=un,password=ps)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/')
            else:
                message = "Unable to login: user not recognised or deactivated"
                
    else:
        form = LoginForm()
    args = {'form':form,'message':message}
    c = RequestContext(request,args)
    t = loader.get_template('sjcpunts/login.html')
    return HttpResponse(t.render(c))
    
def mylogout(request):
    logout(request)
    returnto = request.META['HTTP_REFERER']
    return HttpResponseRedirect(returnto)

def permission_err(request, message="You do not have permission to do that"):
    return error(request, title="Permission Error", catagory="Permission Error", message=message)


def nopage_err(request, message="This page does not exist"):
    return error(request, title="Page not found Error", catagory="No page Error", message=message)

def error(request,title="Error", catagory="General Error", message="An error has occured", opts = {}):
    args = {'title':title,'catagory':catagory, 'message':message}
    #args += opts
    c = RequestContext(request,args)
    t = loader.get_template('sjcpunts/error.html')
    return HttpResponse(t.render(c))