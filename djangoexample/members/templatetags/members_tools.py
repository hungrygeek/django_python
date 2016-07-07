'''
Created on 3 Apr 2013

@author: giles
'''
from django import template
from django.template.base import Node, NodeList, Template, Library,TemplateSyntaxError
from django.template import Context, loader
from members.models import Member
from django.contrib.auth.models import User
register = template.Library()

TINY = 'tiny'
SHORT = 'short'
MED = 'med'
LONG = 'long'

NAME = 'name'
PIC = 'pic'
CARD = 'card'

@register.simple_tag
def member(member,**kwargs):
    if isinstance(member,User):
        member = member.member
    mtype = kwargs.get('mtype','name').lower()
    if mtype in ('name'):
        mtype = NAME
    elif mtype in ('pictures','images','picwall','pic'):
        mtype = PIC
    elif mtype in ('card', 'profile'):
        mtype = CARD
    else:
        mtype = NAME
    
    length = kwargs.get('length','short').lower()
    if length in ('tiny'):
        length = TINY
    elif length in ('short','small'):
        length = SHORT
    elif length in ('med','medium'):
        length = MED
    elif length in ('long','huge'):
        length = LONG
    else:
        length = SHORT
    
    img = kwargs.get('img',"True").lower()
    if img in ("true", "yes", "y","t"):
        img = True
    else:
        img = False
        
    link = kwargs.get('link',"True")
    if link.lower() in ("true", "yes", "y","t"):
        link = True
    else:
        link = False
        
    args = {'m':member,'type':mtype, 'len':length,'img':img,'link':link}
    c = Context(args)
    t = loader.get_template('members/tools/member.html')
    print t.render(c)
    return t.render(c)
        