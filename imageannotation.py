import pygame
import pygamefunctions as p
import sys

p.init()

def drawimage(fn):
    i = p.loadimage(fn)
    p.image(i,(100,100))

eximage = "/home/umar/dog.jpg"

def labelpixels():
    drawimage(eximage)
    #     p.rectangle(700,500,100,50,"red")
    p.text("classify",100,"blue",
           (500,10))

def labelimage():
    drawimage(eximage)
    p.text("cat",100,"blue",
           (100,10))
    p.text("yes",80,"green",
           (500,10))
    p.text("no",80,"red",
           (650,10))

done = False
while not done:
    if sys.argv[1] == "pixel":
        labelpixels()
    elif sys.argv[1] == "image":
        labelimage()

    p.redisplay()

    events = pygame.event.get( )
    for e in events:
        if(e.type == pygame.KEYDOWN):
            if (e.key == pygame.K_ESCAPE):
                done = True
            elif (e.key == pygame.K_q):
                done = True
