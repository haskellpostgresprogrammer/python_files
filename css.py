import umarutils as u

def rules(l,filename):
    return u.writefile(u.flattentostring([[x[0]+" {"+x[1]+":"+x[2]+"}\n"]
                                          for x in l]),filename)

def linkrel(cssfile):
    return "".join(["<link rel=stylesheet href=\"",
                    cssfile,"\" type=\"text/css\">"])

def writelinkrel(htmlfile,cssfile):
    original = list("".join(u.readfile(htmlfile)).partition("<head>"))
    original.insert(2,linkrel(cssfile))
    u.writefile("".join(original),htmlfile)
    print htmlfile+" written"
    
def changelinkrel(htmlfile,cssfile):
    p = "<link rel=stylesheet href="
    original = list("".join(u.readfile(htmlfile)).partition(p))
    original.remove(p)
    firstpart = original[0]
    secondpart = list(original[1].partition(" type=\"text/css\">"))[2:]
    final = "".join([firstpart,linkrel(cssfile),secondpart[0]])
    u.writefile("".join(final),htmlfile)
    print htmlfile+" written"

def haslinkrel(htmlfile):
    p = "<link rel=stylesheet href="
    filedata = list("".join(u.readfile(htmlfile)).partition(p))
    if filedata[1] == "":
        return False
    else:
        return True
