import povray as pv

burnerdiameter = 12
burnerheight = 1
burnerseperation = 1
def burner(x,y,z):
    return pv.cylinder([x,y,z],
                       [x,y+burnerheight,z],
                       burnerdiameter/2,"Silver"),
def burners(x,y,z):
    return [burner(i[0],y,i[1]) for
            i in grid2(10,5,
                       burnerdiameter+burnerseperation)]

import numpy as np
def grid3(x,y,z):
    a = np.mgrid[0:x,0:y,0:z]
    b = [list(i.flatten()) for i in a]
    return zip(b[0],b[1],b[2])
def grid2(x,y):
    a = np.mgrid[0:x,0:y]
    b = [list(i.flatten()) for i in a]
    return zip(b[0],b[1])
def ex():
    return grid2(4,4)
# def grid2(xpos,ypos,xnum,ynum,
#           xlength,ylength,xsep,ysep):
#     xincrement = xlength+xsep
#     yincrement = ylength+ysep
#     xlength = (xnum*xincrement)-xsep
#     ylength = (ynum*yincrement)-ysep
#     xinit = xpos-(xlength/2)
#     yinit = ypos-(ylength/2)
#     return u.flatten1([[[x,y]
#                         for y in
#                         range(yinit,ylength,yincrement)]
#                        for x in
#                        range(xinit,xlength,xincrement)])
# def grid3(xnum,ynum,znum):
#     return u.flatten1(u.flatten1(
#         [[[[x,y,z]
#            for z in range(0,znum*sep,sep)]
#           for y in range(0,ynum*sep,sep)]
#          for x in range(0,xnum*sep,sep)]))

# use scara or parallel flexpicker  robot for
# cooking robot

def run():
    pv.runpov([
        pv.incfiles(),
        #         pv.plane("y",0,"Green"),
        burners(0,0,0),
        pv.camera([0,100,-100],[0,0,0]),
        pv.lightsource([0,150,-150],"White"),
        ],"cookingrobot")
    pv.display("cookingrobot")
