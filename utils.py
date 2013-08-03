import datetime
import time
import functional
import re

def now():
    return datetime.datetime.now()

def flatten(x):
    return functional.flatten(x)
def flatten1(x):
    return functional.flatten1(x)

def flattentostring(l):
    flatlist = functional.flatten(l)
    flatlistnone = []
    for x in flatlist:
        if isinstance(x,str):
            flatlistnone.append(x)
        else:
            flatlistnone.append("none")
    return "".join(flatlistnone)

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

def epochtime():
    return time.time()

def randomitem(thelist,number):
    import random
    return [random.choice(thelist) for x in range(number)]

def deletebeforeaftertext(text,before,after):
    a = text.replace(before,"")
    return a.replace(after,"")
def underlinespaces(x):
    return x.replace(" ","_")
def spaceunderlines(x):
    return x.replace("_"," ")
def underscore_downcase(x):
    return x.replace(" ","_").lower()

def tocsv(thelist):
    return "\n".join([";".join(x) for x in thelist])
def fromcsv(thelist):
    return [x.split(";") for x in thelist.split("\n")]

def kv(k,l):
    return [x[1:] for x in l if x[0] == k][0]
