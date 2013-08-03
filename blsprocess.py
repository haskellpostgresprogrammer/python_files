import umarutils as u
import os
import postgres as pg
import html as h
import automatejobs

def capwords(x):
    return " ".join([x.capitalize() for x in x.split(" ")])

def sql(query):
    return pg.pgsql("mypersonal",query)

homedir = "/home/umar/"
blsdir = "bls/indexprocess/processjobs/"

def files():
    return [homedir+blsdir+x for x in
            os.listdir(homedir+blsdir)]

def processonefile(b):
    c = "".join(u.readfile(b))
    d = c.replace("\n"," ").replace("\t"," ").replace("\r"," ")
    e = "".join(d.replace("<","<---").replace(">","--->"))
    f = [x.split(">") for x in e.split("<")]
    g = [x for x in u.flatten(f)
         if x.startswith("---") != True]
    h = "".join(g).replace(".",".\n").split("\n")
    i = u.flatten([x.split("  ") for x in h])
    j = [x.lstrip().rstrip() for x in i if x != '']
    return j

def jobtitle(title):
    a = title.split("/")
    b = a[-1].replace(".htm","").replace("-"," ")
    return b

def blstabsepfile():
    u.writefile("","/home/umar/blstabsepfile")
    a = [[x,jobtitle(x)] for x in files()]
    for jobfile in a:
        jobsentences = processonefile(jobfile[0])
        for sentence in jobsentences:
            u.appendfile(jobfile[1]+"\t"+sentence+"\n",
                         "/home/umar/blstabsepfile")
    return 

def numofsentences():
    return sql("select count(*) from blssentences;")

def numuniqsentences():
    return sql("select count(distinct sentence) from blssentences;")

def jobuniqsentences(job):
    return sql("select sentence from blssentences where job = '"+job+"' except select sentence  from blssentences where job <> '"+job+"';")

def jobtitles():
    return sql("select distinct job from blssentences;")

def jobsprint():
    

# create function blsjobuniqsentences(text)
# returns setof as
# $$ select job, sentence from blssentences
# where job = $1
# except
# select job, sentence from blssentences
# where job <> $1;
# $$ language sql;

def css():
    return "\n".join([x[0]+" {"+x[1]+" : "+x[2]+"}" for x in [
        ["body","background-color","lightblue"],
        ["body","margin-left","3%"],
        ["body","margin-right","3%"],
        [".col1","color","blue"],
        [".col2","color","darkblue"],
        ["h1","color","orange"],
        ["h2","color","magenta"],
        ["h3","color","red"],
        [".borderedtable table td","border","solid"],
        ]])

thetitle = "How To Automate All Jobs"
filename = "blsjobs"
filenamehtml = filename+".html"
filenamecss = filename+".css"

def exporthtml():
    a = h.htmlwithstylesheet(thetitle,
                             "",
                             thebody(),
                             filename)
    u.writefile(a,homedir+filenamehtml)
    u.writefile(css(),homedir+filenamecss)
def thebody():
    return [h.h1("How to automate all jobs"),
            bynum(),
            ]

# def jobtitles():
#     return [[capwords(x[0]),h.br()] for x in
#         sql("select distinct job from blssentences;")]

def formatjobs(l):
    return [[h.h3(capwords(x[0])),
             formatfloats(x[1:]),
             jobcontents(x[0])
             ]
            for x in l]
def formatnums(x):
    if x > 1000000000:
        return str(x/1000000000)+" billion"
    elif x > 1000000:
        return str(x/1000000)+" million"
    elif x > 1000:
        return str(x/1000)+" thousand"
    elif x == 0:
        return "no information"
    else:
        return str(x)
def formatfloats(f):
    if len(f) == 2:
        return [
            formatnums(f[0])," dollars",h.br(),
            formatnums(f[1])," jobs",h.br(),
            formatnums(f[0]*f[1])," dollars market size",
            h.br()
            ]
        return [[formatnums(x),h.br()] for x in f]
    else:
        return [formatnums(f[0])," dollars"]
    
def bynum():
    return [h.h2("Highest to lowest number of jobs"),
            formatjobs(automatejobs.jobhighnum())]

def jobs():
    return automatejobs.jobs()

def jobcontents(job):
    data = [y for y in jobs() if y[0] == job]
    return [[x,h.br()] for x in data[0][2]]
