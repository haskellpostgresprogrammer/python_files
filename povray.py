import umarutils as u

def writepovfile(l,f):
    u.writefile("".join(u.flatten(l)),f)
    return f+" written"
def dn(x):
    return x+"\n\n"
def obj(title,body):
    return dn(title+" {\n"+"\n".join(body)+"\n}")
def vec(x):
    return "<"+",".join([str(x[0]),str(x[1]),str(x[2])])+">"
def includefile(x):
    return "#include \""+x+".inc\""
def includefiles(l):
    return dn("\n".join([includefile(x) for x in l]))
def incfiles():
    return includefiles(["colors",
                         "shapes","textures","skies"])
def camera(locationv,lookatv):    
    return obj("camera",
               ["location "+vec(locationv),
                "look_at "+vec(lookatv)])
def lightsource(location,color):
    return obj("light_source",[vec(location),color])

def pigment(color):
    return obj("pigment",[color])
def texture():
    return obj("texture",[])
def finish():
    return obj("finish",[])
def normal():
    return obj("normal",[])
def plane(normal,distance,color):
    return obj("plane",
               [str(normal),str(distance),
                pigment(color)])
def skysphere():
    return obj("sky_sphere",["S_Cloud5"])

def runpov(l,f):
    a =  writepovfile(u.flatten(l),
                      "/home/umar/povrayfiles/"+f+".pov")
    u.shellcommand(["povray",
                    "-O/tmp/"+f+".png",
                    "/home/umar/povrayfiles/"+f+".pov"])
    u.shellcommand(["cp",
                    "/tmp/"+f+".png",
                    "/home/umar/public_html/"+f+".png"])

def square():
    return
def circle():
    return
def image():
    return
def box(corner1,corner2,color):
    return obj("box",
               [vec(corner1),vec(corner2),
                pigment(color)])

def text2d():
    return

def sphere(center,radius,color):
    return obj("sphere",
               [vec(center),str(radius),
                pigment(color)])

def cylinder(bottom,top,radius,color):
    return obj("cylinder",
               [vec(bottom),vec(top),str(radius),
                pigment(color)])

def display(f):
    u.shellcommand(["xli","-fillscreen",
                    "/home/umar/public_html/"+f+".png"])
    u.shellcommand(["xli","-onroot","-fillscreen",
                    "/home/umar/public_html/"+f+".png"])

def translate(x,y,z):
    return "".join(["translate ",vec([x,y,z])])
def rotatex(x):
    return "".join(["rotate ",vec([x,0,0])])
def rotatey(x):
    return "".join(["rotate ",vec([0,x,0])])
def rotatez(x):
    return "".join(["rotate ",vec([0,0,x])])
def scale(x,y,z):
    return "".join(["scale ",vec([x,y,z])])

def union(l):
    return obj("union",l)
def merge(l):
    return obj("merge",l)
def intersection(l):
    return obj("intersection",l)
def difference(l):
    return obj("difference",l)
