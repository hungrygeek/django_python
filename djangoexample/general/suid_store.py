'''
Created on 26 Mar 2013

@author: giles
'''
class suidStore():
    
    def __init__(self, trimlen=20):
        self.suids = []
        self.trimlen = trimlen
    
    def check(self,suid):
        if suid in self.suids:
            return False
        else:
            return True
    def add(self, suid):
        self.suids.append(suid)
    
    def rm(self, suid):
        self.suids.remove(suid)
        
    def trim(self):
        while len(self.suids) > self.trimlen:
            self.suids.pop(0)