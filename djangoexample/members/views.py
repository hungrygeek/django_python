# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import  loader, RequestContext
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from members.models import Member
from comments.models import Comment
from comments.comment_utils import generateView

USER_COMMENT_HISTORY = 8

@login_required(login_url='/login/')
def detail(request,username):
    user = None
    message = ""
    isme = False
    r_comments=[]
    try:
        tuser = User.objects.get(username__exact=username)
        if tuser is not None:
            if tuser.is_active:
                user = tuser
                r_comments=Comment.objects.filter(submittedby=user.member).order_by('-submittedtime')[:USER_COMMENT_HISTORY]
                cgen = generateView(r_comments,request, parent_link=True)
            else:
                message = "User is inactive"
        else:
            message = "User not found"
    except:
        message = "User not found"
    args = {'user':user,'message':message,'cgen':cgen}
    c = RequestContext(request,args)
    t = loader.get_template('members/individual.html')
    return HttpResponse(t.render(c))


@login_required(login_url='/login/')
def index(request):
    committee = []
    other_users = []
    ms = Member.objects.all()
    com = Group.objects.get(name='committee')
    committee = [u.member for u in com.user_set.all()]
    #other_users = ms
    for m in ms:
        if m.user.is_active:
            if not m in committee:
                other_users.append(m)
            
    args = {'committee':committee,'other_users':other_users}
    c = RequestContext(request,args)
    t = loader.get_template('members/index.html')
    return HttpResponse(t.render(c))