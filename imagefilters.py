from PIL import Image                        
import linalgautoencoder as ae

obdir = "/otherdisk2/data/obamaspeech/"
imgname = "one.jpg"
eximg = obdir+imgname

def getimage(filename):
    return Image.open(filename)

def imagesizes():
    return [[x*x,((x*x)/3)*2] for x in range(5,20)]

def imageresizes(pilimage):    
    for x in imagesizes():
        print pilimage.resize(tuple(x))

def image2text(pilimage):
    return list(pilimage.getdata())

def ex():
    return len(image2text(getimage(eximg)))

def decisiontreetrain():
    return
def decisiontreeclassify():
    return

def linearclassificationtrain():
    return
def linearclassificationclassify():
    return

def autoencodertrain(shrinkage,data,linearity):
    width = len(data[0])
    shrinkby = int(shrinkage*width)
    if linearity == "linear":
        return
    if linearity == "nonlinear":
        return
    return
def autoencoderencode():
    return


def feedforwardnetwork():
    return
def ensemble():
    return
def randomforests():
    return
def supportvectormachine():
    return

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

import numpy as np
import os
from matplotlib import pyplot as plt

def showarray(a):
    plt.imshow(a)
    plt.show()

def getarray():
    i = getimage(eximg)
    a = np.asarray(i)
    return a

def splotches(shape):
    a = np.random.random(shape)
    b = np.reshape(a,shape[0]*shape[1])
    bins = np.array([0.5,1.0])
    inds = np.digitize(b,bins)    
    return np.reshape(inds,shape)

def splotches2(shape):
    a = splotches(shape)
    b = splotches(shape)
    return a*b

def splotchimage(imgarr):
    x = imgarr.shape[0]
    y = imgarr.shape[1]    
    r = splotches2((x,y))
    rr = np.dstack((r,r,r))
    return np.add(imgarr,rr)

def showimage():
    showarray(getarray())

def getandshowgray():
    a = np.asarray(Image.open(eximg))
    gray = a.mean(axis=2)
    return gray
