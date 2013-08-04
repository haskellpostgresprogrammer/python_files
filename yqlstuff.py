import yql
import umarutils as u
import json

def ex():
    y = yql.Public()
    res = y.execute("select * from upcoming.events where woeid in (select woeid from geo.places where text='London')")
    return res

def showtables():
    y = yql.Public()
    env = "http://datatables.org/alltables.env"
    query = "Show tables;"
    res = y.execute(query,env=env)
    return res

def envprint(a):
    f = open("/home/umar/yqltables","w")
    for x in a.rows:
        f.write(str(x))
        f.write("\n")
    f.close()
    
def loadtables():
    a = u.readfile("/home/umar/yqltables")
    curls = [eval(x.replace("\n","")).items()
             for x in a if x.startswith("{") == True]
    strings = [x.replace("\n","")
               for x in a if x.startswith("{") != True]
    return [curls,strings]

def tablecontents():
    return [str(x[0][1]) for x in loadtables()[0]]
def tableyahoos():
    return loadtables()[1]
def tableparts():
    a = tablecontents()
    b = tableyahoos()
    c = a+b
    return [x.split(".") for x in c]
def tableroots():
    a = [x[0] for x in tableparts()]
    return list(set(a))
def tablesearch(s):
    return [x[1:] for x in tableparts()
            if x[0] == s]
