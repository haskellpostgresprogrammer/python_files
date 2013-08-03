import cPickle
import os
import subprocess
import re
import fnmatch
import glob
import functional
import time
import datetime
import urllib2
# import html5lib

def writefile(string,filename):
    f = open(filename,"w")
    f.write(string)
    f.close()
def writefileifnotexists(string,filename):
    if os.path.isfile(filename) == False:
        writefile(string,filename)
    elif os.path.isfile(filename) == True:
        print "file exists"
def writefilebinary(data,filename):
    f = open(filename,"wb")
    f.write(data)
    f.close()
def appendfile(string,filename):
    f = open(filename,"a")
    f.write(string)
    f.close()
def readfile(filename):
    f = open(filename,"r")
    l = f.readlines()
    f.close()
    return l
def readfilenn(filename):
    return [x.replace("\n","") for x in readfile(filename)]
def writepickle(object,filename):
    """Write a pickle, object filename"""
    f = open(filename,"w")
    cPickle.dump(object,f)
    f.close()
def readpickle(filename):
    f = open(filename,"r")
    p = cPickle.load(f)
    f.close()
    return p

def flattentostring(l):
    flatlist = functional.flatten(l)
    flatlistnone = []
    for x in flatlist:
        if isinstance(x,str):
            flatlistnone.append(x)
        else:
            flatlistnone.append("none")
    return "".join(flatlistnone)

def writeflatextension(datalist,filename,extension):
    writefile(flattentostring(datalist),filename+"."+extension)
    print "written "+filename+"."+extension

def matchingfiles(directory,pattern):
    return fnmatch.filter(os.listdir(directory),pattern)
def matchingfilesnotildes(directory,pattern):
    all = matchingfiles(directory,pattern)
    tildes = matchingfiles(directory,"*~")
    hidden = matchingfiles(directory,".*")
    finalX = list(set(all) - set(tildes))
    final = list(set(finalX) - set(hidden))
    return final

def shellcommand(commandargs):
    process = subprocess.Popen(commandargs,
                               shell=False,
                               stdout=subprocess.PIPE)
    comm = process.communicate()
    output = comm[0]
    return output
def backgroundcommand(commandargs):
    p = subprocess.Popen(commandargs,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT) 

def bashcommand(commandargs):
    process = subprocess.Popen(commandargs,
                               shell=True,
                               stdout=subprocess.PIPE)
    comm = process.communicate()
    output = comm[0]
    print output

    
def aptsearch(name):
    data = shellcommand(["apt-cache","search",name])
    newlines = data.split("\n")[:-1]
    namedesc = [x.split(" - ",1) for x in newlines]
    return namedesc

def matchlist(reg,stringlist):
    l = []
    for x in stringlist:
        m = re.search(reg,x)
        if m:
            l.append(x)
    return l
def matchstring(reg,string):
    x = matchlist(reg,[string])
    if x == []:
        return False
    else:
        return True

def removenewlines(stringlist):
    return [x.replace("\n","") for x in stringlist]

def flatten(x):
    return functional.flatten(x)
def flatten1(x):
    return functional.flatten1(x)

def filestonamelists(files):
    filecontents = [[x,readfile(x)] for x in files]
    nonewlines = [[x[0],removenewlines(x[1])]
                  for x in filecontents]
    fileslists = [[x[0],x[1]] for x in nonewlines]
    return fileslists

def productiterator(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
def product(l1,l2):
    return map(list,list(productiterator(l1,l2)))
def cyclicpairs(l):
    return map(list,functional.cyclic_pairs(l))
def permutations2(listoflists):
    length = len(listoflists)
    permnumbers = cyclicpairs(range(length))
    permlist = [[listoflists[x[0]],listoflists[x[1]]]
              for x in permnumbers]
    perms = [product(x[0],x[1]) for x in permlist]
    flat1perms = flatten1(perms)
    return flat1perms

def substitute(substitutes,item):
    return [x[1] for x in substitutes if item == x[0]]
def substitutelist(substitutes,l):
    return map(flatten,
               [[substitute(substitutes,x[0]),
                 substitute(substitutes,x[1])]
                for x in l])

def remove(lista,listb):
    return list(set(lista) - set(listb))
def removedups(l):
    return functional.remove_duplicates(l)

def randomitem(thelist,number):
    import random
    return [random.choice(thelist) for x in range(number)]

def files(pattern):
    return glob.glob(pattern)

def deletebeforeaftertext(text,before,after):
    a = text.replace(before,"")
    return a.replace(after,"")
def underlinespaces(x):
    return x.replace(" ","_")
def spaceunderlines(x):
    return x.replace("_"," ")

def epochtime():
    return time.time()
def datetimename(x):
    return x+"_"+str(datetime.datetime.now())[:19].replace(
        " ","-").replace(":","-").replace("-","_")

def tocsv(thelist):
    return "\n".join([";".join(x) for x in thelist])
def fromcsv(thelist):
    return [x.split(";") for x in thelist.split("\n")]    

def kv(k,l):
    return [x[1:] for x in l if x[0] == k][0]

def subdirs(name):
    return [x for x in os.listdir(name)
            if os.path.isdir(name+x) == True]

def latestfilemodificationtime(path):
    return list(os.stat(path))[8]

import subprocess
def shellcommand(commandargs):
    process = subprocess.Popen(commandargs,
                               shell=False,
                               stdout=subprocess.PIPE)
    comm = process.communicate()
    output = comm[0]
    return output
def backgroundcommand(commandargs):
    p = subprocess.Popen(commandargs,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT) 

def getpass():
    return readfilenn("/home/umar/pass")

def asciistrings(l):
    return [[y.encode("ascii") for y in x] for x in l]

def geturl(url):
    request = urllib2.Request(url)
    opener = urllib2.build_opener()
    request.add_header('User-Agent',
                       'reddit is the best 121')
    urldata = opener.open(request).read()
    return urldata
#     urllib._urlopener = AppURLopener()
#     a = urllib.urlopen(url)
#     b = a.read()
#     a.close()
#     return b

def parsehtml(filename):
    a = "".join(readfile(filename))
    b = html5lib.parse(a,treebuilder="lxml")
    return b

def grepfiles(s,d):
    return shellcommand(["grep","-nr",s,d])

