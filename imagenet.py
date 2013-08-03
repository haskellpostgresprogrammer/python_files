import umarutils as u
import urllib
import os
import randomnetworks as rn
import time

imagenetdir = "/otherdisk2/data/imagenet/"
wnidsfile = imagenetdir+"words.txt"

def wordstownid(words):
    filedata = u.readfilenn(wnidsfile)
    for x in filedata:
        y = x.split("\t")[1]
        if y == words:
            return x.split("\t")[0]

def downloadurls(word):
    wnid = wordstownid(word)
    filename = imagenetdir+word.replace(" ","_")+".urls"
    urllib.urlretrieve("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid="+wnid,filename)
    data = u.readfilenn(filename)
    if data[0].startswith("http://") == False:
        os.remove(filename)
        print "file contains no urls, removed"
    else:
        print "saved"

def wordshow(word):
    filedata = u.readfilenn(wnidsfile)
    data = []
    for x in filedata:
        if word in x:
            data.append(x.split("\t")[1])
    return data

def urlfiles():
    files =  [imagenetdir+x for x in os.listdir(imagenetdir)
            if x.endswith(".urls") == True]
    return [[x,len(u.readfile(x))] for x in files]

def makeimagedirs():
    urls = [x.replace(".urls","")
                for x in os.listdir(imagenetdir)
                if x.endswith(".urls") == True]
    existing = u.subdirs(imagenetdir)
    tocreate = u.remove(urls,existing)
    for x in tocreate:
        os.mkdir(imagenetdir+x)
        print x+" created"

def downloadimages():
    
    wget -i -nc 
