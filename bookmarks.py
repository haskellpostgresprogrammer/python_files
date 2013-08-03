# cron
# todo
# incomplete

import umarutils as u

def bookmarks():
    return [x.split(",")
        for x in u.readfilenn("/home/umar/bookmarks")]

def reddits():
    return [[y[0],"".join(y[1:]).split(",")] for y in
            [x.split("\n") for x in
             "".join(u.readfile("/home/umar/reddits")).split("\n\n")]]

def googlevideosearchattribute(a):
    dur = "dur:"
    time = "qdr:"
    if a == "anyduration":
        return
    elif a == "shortduration":
        return dur+"s"
    elif a == "mediumduration":
        return dur+"m"
    elif a == "longduration":
        return dur+"l"
    elif a == "anytime":
        return
    elif a == "pasthour":
        return time+"h"
    elif a == "past24hours":
        return time+"d"
    elif a == "pastweek":
        return time+"w"
    elif a == "pastmonth":
        return time+"m"
    elif a == "pastyear":
        return time+"y"
    else: return

def googlesitesearchvideo(s):
    if len(s) == 2:
        return "+".join([s[0].replace(" ","+"),"site:"+s[1]])
    else:
        return "+".join(s[0].replace(" ","+"))

def googlevideosearches():
    f = "".join(u.readfile("/home/umar/googlevideosearch"))
    parts = f.partition("\n\n") 
    sites = [x.split(",") for x in parts[0].split("\n")]
    searches = [x.split(",") for x in parts[2].split("\n")][:-1]
    for x in searches:
        for y in sites:
            if x[1] == y[1]:
                x[1] = y[0]
    a = [[[x[0],x[1]],x[2:]] for x in searches]
    return h.tabularize([
        h.newtabopen("".join(["http://www.google.com/search?q=",
                              "&".join([googlesitesearchvideo(x[0]),
                                        "tbm=vid",
                                        "tbs="+",".join([
        googlevideosearchattribute(y)
        for y in x[1]]),
                                        ])]),x[0][0])
        for x in a],2)

def googlenewsurl(s):
    return "".join(["http://www.google.com/search?q=",
                    s.replace(" ","+"),"&hl=en&gl=us&tbm=nws"])

def googlenewsurls():
    return [h.newtabopen(googlenewsurl(x),x)
            for x in u.readfilenn("/home/umar/googlenewssearches")]

import html as h
import umarutils as u
br = h.br()
def html():
    return h.h("my bookmarks",[
        h.returntohome(),
        [[h.newtabopen(x[1],x[0]),h.space()] for x in bookmarks()],br,
        [[br,h.newtabopen(x,x)]
         for x in
         u.readfilenn("/home/umar/addedbookmarks")],br,
        "reddits",br,
        h.tabularize([h.newtabopen("http://reddit.com/r/"+"+".join(x[1]),
                                  x[0]) for x in reddits()],2),br,
        "google news searches",br,
        h.tabularize(googlenewsurls(),2),
        "google video searches",br,
        googlevideosearches(),
        h.returntohome()
        ])
