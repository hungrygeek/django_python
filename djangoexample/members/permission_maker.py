'''
Created on 28 Mar 2013

@author: giles
'''

from django.contrib.auth.models import User, Group, Permission

perms_committee = ['user_create',
                   'user_view_active',
                   'user_edit_self',
                   'user_edit_all',
                   'user_fdel_all',
                   'group_create_edit',
                   'ticket_create',
                   'ticket_view_all',
                   'ticket_view_deld',
                   'ticket_comment',
                   'ticket_comment_del',
                   'ticket_comment_del_self',
                   'ticket_comment_edit_all',
                   'ticket_close',
                   'ticket_fdel_norm',
                   'file_view_all',
                   'file_view_deld',
                   'file_create_small',
                   'file_create_large',
                   'file_edit_self',
                   'file_edit_all',
                   'file_fdel_self',
                   'file_fdel_all',
                   'file_rdel_all',
                   'file_edit_icons',
                   'punt_create',
                   'punt_view_current',
                   'punt_view_all',
                   'punt_edit',
                   'punt_add_ticket',
                   'punt_view_maint',
                   'punt_decomission',
                   'punt_fdel',
                   'accounts_view_all',
                   'accounts_summarise',
                   ]

perms_treasurer = ['accountitem_create',
                   'accountitem_edit',
                   'accounts_view_all',
                   'accounts_view_deld',
                   'accountitem_fdel',
                   'accounts_summarise',
                   'account_create',
                   'account_edit',
                   ]

perms_members = [  'user_view_active',
                   'user_edit_self',
                   'ticket_create',
                   'ticket_view_all',
                   'ticket_comment',
                   'ticket_comment_del_self',
                   'file_view_all',
                   'file_create_small',
                   'file_edit_self',
                   'file_fdel_self',
                   'punt_view_current',
                   'punt_view_all',
                   'punt_add_ticket',
                   'punt_view_maint',
                   ]

perms_exmembers = ['user_edit_self',
                   'ticket_view_all',
                   'file_edit_self',
                   'file_fdel_self',
                   'punt_view_current',                   
                   ]

perms_showoff = [  'ticket_view_all',
                   'punt_view_current', 
                 ]


permissions = {'user_create'        :'auth.add_user,members.add_member',
               'user_view_active'   :'members.view_active',
               'user_edit_self'     :'members.edit_self',
               'user_edit_all'      :'members.edit_all,auth.change_user',
               'user_fdel_all'      :'members.fdel_all',
               'user_rdel_all'      :'members.delete_all',
               'group_create_edit'  :'auth.add_group,auth.change_group,auth.delete_group',
               'ticket_create'      :'ticket.add_ticket',
               'ticket_view_all'    :'ticket.view_all',
               'ticket_view_deld'   :'ticket.view_deleted',
               'ticket_comment'     :'comments.create_ticket',
               'ticket_comment_del' :'comments.delete_ticket',
               'ticket_comment_del_self'    :'comments.delete_ticket_self',
               'ticket_comment_edit_self'   :'comments.edit_ticket_self',
               'ticket_comment_edit_all'    :'comments.edit_ticket_all',
               'ticket_close'       :'ticket.close',
               'ticket_fdel_norm'   :'ticket.fdel_norm',
               'ticket_fdel_acc'    :'ticket.fdel_acc',
               'ticket_rdel_norm'   :'ticket.delete_norm',
#               'rota_bailing_view'  :'events.rota_bailing_view',
#               'rota_bailing_edit'  :'events.rota_bailing_edit',
#                'event_create'        :'events.event_create',
#                'event_edit'        :'events.event_edit',
#                'event_comment'    :'events.event_comment',
               'file_view_all'      :'files.view_file_all',
               'file_view_deld'     :'files.view_file_deleted',
               'file_create_small'  :'files.create_file_small',
               'file_create_large'  :'files.create_file_large',
               'file_edit_self'     :'files.edit_file_self',
               'file_edit_all'      :'files.edit_file_all',
               'file_fdel_self'     :'files.fdel_file_self',
               'file_fdel_all'      :'files.fdel_file_all',
               'file_rdel_all'      :'files.rdel_file_all',
               'file_edit_icons'    :'files.add_icon,files.change_icon,files.delete_icon',
               'punt_create'        :'punts.punt_create',
               'punt_view_current'  :'punts.punt_view_current',
               'punt_view_all'      :'punts.punt_view_all',
               'punt_view_maint'    :'punts.punt_view_maintenance',
               'punt_edit'          :'punts.punt_edit',
               'punt_add_ticket'    :'punts.punt_add_ticket',
               'punt_decomission'   :'punts.punt_decomission',
               'punt_fdel'          :'punts.punt_fdel',
               'accountitem_create' :'accounts.accountitem_create',
               'accountitem_edit'   :'accounts.accountitem_edit',
               'accounts_view_all'  :'accounts.view_all',
               'accounts_view_deld' :'accounts.view_deleted',
               'accountitem_fdel'   :'accounts.accountitem_fdel',
               'accounts_summarise' :'accounts.summarise',
               'account_create'     :'accounts.account_create',
               'account_edit'       :'accounts.account_edit',
               }

def check_makeGroups():
    try:
        com = Group.objects.get(name='committee')
    except:
        com = Group(name='committee')
        com.save()
    set_group_permissions(com,perms_committee)
    #TODO Add rest
    

def set_group_permissions(gin,gperms):
    for p in gperms:
        if p in permissions:
            pl = permissions[p].split(',')
            for pa in pl:
                parts = pa.split('.')
                #TODO: Add content type finder and permission sorter