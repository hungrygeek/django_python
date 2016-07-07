'''
Created on Mar 19, 2013

@author: giles
'''

from ticket.models import File
def getfilesfromfields(listoffiles, autofile):
    out = []
    
    fs = autofile.split(',')
    for f in fs:
        try:
            f = int(f)
            af = File.objects.get(id=f)
            out.append(af)
        except:
            pass
            
    out += listoffiles