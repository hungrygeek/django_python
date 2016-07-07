'''
Created on Mar 13, 2013

@author: giles
'''
import base64
import struct

 
def build_timestamp(time):
    """
    Return a 6 chars url-safe timestamp
    """
    return base64.urlsafe_b64encode(struct.pack("!L",int(time)))[:-2]
 
def read_timestamp(t):
    """
    Convert a 6 chars url-safe timestamp back to time
    """
    return struct.unpack("!L",base64.urlsafe_b64decode(t+"=="))[0]

