import pygame
import pygamefunctions as p
import timeinfo

p.init()

def neuron(radius,x,y,outlinecolor,fillcolor):
    p.circle(outlinecolor,(x,y),radius)
    p.circle(fillcolor,(x,y),radius-2)

def layer(radius,num,spacing,xi,y,outlinecolor,
          fillcolor):
    totallength = ((radius*2)*num)+((num-1)*spacing)
    x = xi - (totallength/2)
    for i in range(num):
        neuron(radius,x,y,outlinecolor,fillcolor)
        x = x+spacing+radius+radius

def layer3(radius,num,hiddennum,spacing,
           layerspacing,x,y,topxmove):
    layerspace = layerspacing+radius+radius    
    layer(radius,num,spacing,x-topxmove,
          y,"blue","black")
    layer(radius,hiddennum,spacing,x,
          y+layerspace,"red","black")
    layer(radius,num,spacing,x,
          y+layerspace+layerspace,"blue","black")

slidepos = 0

def slidetoplayer():
    global slidepos
    global done
    initialx = 300
    layer3(10,21,10,5,20,initialx,300,slidepos)
    slidepos = slidepos + 1
    if slidepos > (initialx+500):
        done = True

done = False
while not done:
    slidetoplayer()
    p.redisplay()
    
    events = pygame.event.get( )
    for e in events:
        if(e.type == pygame.KEYDOWN):
            if (e.key == pygame.K_ESCAPE):
                done = True
            elif (e.key == pygame.K_q):
                done = True

