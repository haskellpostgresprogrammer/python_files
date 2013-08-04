import pygameutils as pu
import time

textposh = -100
def scrollingright(text,size,vpos,color,speed):
    global textposh
    pu.drawtext(text,size,(textposh,vpos),color)
    if textposh < 1024:
        textposh = textposh + speed
    else:
        textposh = -100

textposv = 100
def scrollingdown(text,size,hpos,color,speed):
    global textposv
    pu.drawtext(text,size,(hpos,textposv),color)
    if textposv < 650:
        textposv = textposv + speed
    else:
        textposv = 100

rightcounter = 0

def scrollingrightlist():

    return

leftcounter = 0

def scrollingdownlist():
    return

def alist():
    return [x for x in range(100)]

def scrollingexample():
    scrollingright("ideas",50,100,"red",1)
    ideassize = pu.textsize("ideas",50)
    scrollingright(str(ideassize[0])+"w",50,130,"red",1)
    scrollingright(str(ideassize[1])+"h",50,160,"red",1)

    scrollingdown("lists",50,100,"blue",1)
