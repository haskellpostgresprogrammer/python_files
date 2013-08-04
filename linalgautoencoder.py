import numpy as np
import scipy.optimize as opt
import os
import random

def collapse(v):
    return [sum(x) for x in v]

def randomfetch(datafile):
    f = open(datafile,"r")
    fsize = os.stat(datafile)[6]
    f.seek(random.randint(0,fsize-1))
    #dont use the first readline since it may fall in the middle of a line
    file.readline()
    #this will return the next (complete) line from the file
    line = file.readline()
    return line

def encode(coeffs,biascoeffs,num,inputv):
    out = []
    for x in range(num):
        z = []
        y = coeffs[x]*inputv
        yz = collapse(y)
        if yz > biascoeffs[x]:
            z[x] = 1
        else:
            z[x] = 0
        out.append(z)        
    return out

def decode(coeffs,num,inputv):
    out = []
    for x in range(num):
        y = coeffs[x]*inputv
        yz = collapse(y)
        out.append(yz)        
    return out

# middlenum =
# datafile =
# datasize = 
def transcode(v):    
    e = encode(v[:middlenum],
               v[middlenum:(2*middlenum)],
                middlenum,randomfetch(datafile))
    d = decode(v[datasize:],datasize,e)
    return

def autoencode(initialv):
    r = opt.minimize(transcode,
                     initialv,method="Anneal")
    return r
