'''
Created on Mar 19, 2013

@author: giles
'''

#import django.core.files


userfile_icon_root = "userfiles/icons"

imgtypes = ['png','PNG', 'jpg', 'jpeg', 'bmp', 'svg','JPG']

dficonurl = 'icons/default.png'


NOICON = 0
DFICON = 1
EXICON = 2 # The iconlink points to the icon
CUICON = 3 # The iconfile points to the icon

def getfilesfromfields(listoffiles, autofile):
    out = []
    
    fs = autofile.split(',')
    for f in fs:
        try:
            f = int(f)
            from files.models import File
            af = File.objects.get(id=f)
            out.append(af)
        except:
            pass
            
    out += listoffiles
    return out
    
def makeiconfile(file):
    return file