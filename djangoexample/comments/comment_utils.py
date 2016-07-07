'''
Created on 26 Mar 2013

@author: giles

'''
from random import random
import time
from general.chartimestamp import build_timestamp
from comments.forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext

def makeCF(user,parent_type,parent_id):
    suid = build_timestamp(time.time())
    if not user == None:
        suid += user.username
    suid += str(random())
    suid = str(hash(suid))
    
    data = {'parent':(parent_type + ":" + str(parent_id)),'suid':suid}
    return CommentForm(initial=data)

def generateView(commentlist,request=None,stylesheet='css/comment_display.css',can_comment=True, parent_link=False):
    if(can_comment == True and request == None):
        return ""
    c_indivs = recurseCommentView(commentlist, can_comment=can_comment,parent_link=parent_link)
    args = {'c_indivs':c_indivs}
    if can_comment:
        args['hid_cform'] = makeCF(request.user,'',0)
    if parent_link:
        args['c_display_link'] = True
    c = {}
    if not request == None:
        c = RequestContext(request,args)
    else:
        c = Context(args)
    t = loader.get_template('comments/display_wrapper.html')
    rendered = t.render(c)
    #print rendered
    return rendered
        
def recurseCommentView(commentlist, can_comment,parent_link=False):
    cs_rendered = []
    for c in commentlist:
        sc = c.subcomments.all()
        subs = None
        if sc:
            subs = recurseCommentView(sc,can_comment)
        c = Context({'c':c,'subs':subs,'c_display_link':parent_link,'can_comment':can_comment})  
        t = loader.get_template('comments/display_individual.html')
        cs_rendered.append(t.render(c))
    c = Context({'cs_rendered':cs_rendered,'can_comment':can_comment})    
    t = loader.get_template('comments/display.html')
    return t.render(c)
        