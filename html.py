# app engine library

import utils as u
import math

def localurl():
    return "http://192.168.1.201:8080/"

def opentag(x): return ["<",x,">"]
def closetag(x): return ["</",x,">"]
def t(tag,body):
    return [opentag(tag),body,closetag(tag)]
def attributes(l):
    return [[" ",x[0],"=","\"",x[1],"\""] for x in l]
def ta(tag,attributeslist,body):
    return ["<",tag,
            attributes(attributeslist),
            ">",body,closetag(tag)]
def ota(tag,attributeslist):
    return ["<",tag,attributes(attributeslist),">"]

def ahref(link,text):
    return ta("a",[["href",link]],text)
def newtabopen(link,text):
    return ta("a",[["href",link],["target","_blank"]],text)

def hr():
    return opentag("hr")

def h1(text): return t("h1",text)
def h2(text): return t("h2",text)
def h3(text): return t("h3",text)
def br(): return opentag("br")
def br2(): return [br(),br()]
def space(): return "&nbsp;"
def idclasses(tag,id,classes,body):
    ida = ["id",id]
    classesattribute = ["class"," ".join(classes)]
    return ta(tag,[ida,classesattribute],body)
def div(id,classes,body):
    return idclasses("div",id,classes,body)
def span(id,classes,body):
    return idclasses("span",id,classes,body)

def img(x):
    return ota("img",[["src",x]])

def li(x):
    return t("li",x)
def ol(l):
    return t("ol",[li(x) for x in l])
def ul(l):
    return t("ul",[li(x) for x in l])

def dl(l):
    return t("dl",[[t("dt",x[0]),t("dd",x[1])] for x in l])

def p():
    return "<p>"

def divlink(classes,l):
    return [[div("",classes,ahref(x[0],x[1]))] for x in l]

def stylesheetlink(filename):
    return ota("link",
               [["rel","stylesheet"],
                ["href",filename+".css"],
                ["type","text/css"]])

def cssrules(rules):
    return [[x[0]," {",x[1],":",x[2],"}","\n"] for x in rules]

def html(title,head,body):
    return "".join(u.flatten(t("html",
                               [t("head",[head,t("title",title)]),
                                t("body",body)])))

def h(title,body):
    return htmlwithstylesheet(title,
                              "",
                              body,
                              "/static/main")

def htmlwithstylesheet(title,head,body,stylesheetname):
    return html(title,
                [head,stylesheetlink(stylesheetname)],
                body)

def divstyle(styles,content):
    return ta("div",[["style",[[x[0],":",x[1],";"]
                              for x in styles]]],content)

def link(l,text): return ahref(l,text)

def tag_weigh(x,weight):
    if x==None or x==0:
         x = 1
    return weight * math.log(x, math.e)

def taglist(taglistdups):
    nodups = u.removedups(taglistdups)
    freqs = [[x,len(u.matchlist(x,taglistdups))]
             for x in nodups]
    return freqs

def tagcloud(taglistdups,weight,urlprefix):
    freqs = taglist(taglistdups)
    freqweight = [[x[0],x[1],tag_weigh(x[1],weight)]
                  for x in freqs]
    cloud = [divstyle([["font-size",str(x[2])+"em"],
                       ["float","left"]],
                      link([urlprefix,x[0]],[x[0]," (",str(x[1]),")"]))
             for x in freqweight]
    return cloud

def taglisthtml(taglistdups,urlprefix):
    return [[link([urlprefix,x[0]],[x[0]," (",str(x[1]),")"])]
            for x in taglist(taglistdups)]

def splitlist(thelist,cols):
    return [thelist[x:x+cols]
            for x in range(0,len(thelist),cols)]

def splitlist2(thelist,cols):
    return [" ".join(thelist[x:x+cols])
            for x in range(0,len(thelist),cols)]


def tabularize(thelist,cols):
    return div("",["tabularize"],table(splitlist(thelist,cols)))

def table(tablelist):
    htmltable = []
    rowcount = 0
    for row in tablelist:
        htmlrow = []
        colcount = 0
        for col in row:
            htmlrow.append(
                t("td",
                   div("",
                       ["row"+str(rowcount)+"col"+str(colcount),
                        "row"+str(rowcount),"col"+str(colcount)],
                       col)))
            colcount = colcount + 1
        htmltable.append(t("tr",htmlrow))
        rowcount = rowcount + 1
    return div("",["table"],t("table",htmltable))

def localurlargs(args):
    a = [["&",x[0],"=",x[1]] for x in args]
    return [localurl(),"?",a]

def locallink(text,args):
    return ahref(localurlargs(args),text)

def localstaticlink(text,url):
    return ahref([localurl(),url],text)

def hdiv(app,title,body):
    return h([app," ",title],
             div(u.underscore_downcase(app),
                 [],
                 [div("app",[],localstaticlink(app,"")),
                  div("title",[],locallink(title,[["p",title]])),
                  [div("div"+str(x[0]),[],x[1])
                   for x in zip(range(0,len(body)),body)]]))

def notfound(title,x):
    return h(title,[div("notfound",[],[x+" not found",
                                       br(),returntohome()])])

def returntohome():
    return div("",["returntohome"],ahref("/","home"))

def scriptlink(link):
    return "<script src=\""+link+"\" type=\"text/javascript\"></script>"

def jquerylink():
    return scriptlink("https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js")

# https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js
#     <script src="crowdfunding.js" type="text/javascript"></script>
#     <script src="date.js" type="text/javascript"></script>

def ll(app,text,path):
    return localstaticlink(text,[app+"/"]+path)

def template(app,header,l):
    return htmlwithstylesheet(app,"",[
        ll(app,h1(header),[""]),
        l
        ],app)
