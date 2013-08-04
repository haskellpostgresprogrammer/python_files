import time
import datetime
import string
import random
import pygame

screenwidth = 800
screenheight = 600

def colors(color):
    return pygame.color.THECOLORS[color]

def display(obj,location):
    screen.blit(obj,location)

def text(text,size,color,location):
    font = pygame.font.Font(None,size)
    display(font.render(text,1,colors(color)),
            location)

def rectangle(x,y,w,h,color):
    r = pygame.rect.Rect(x,y,w,h)    
    pygame.draw.rect(screen,colors(color),r)

def circle(color,position,radius):
    pygame.draw.circle(screen,
                       colors(color),position,radius)

def loadimage(path):
    return pygame.image.load(path)

def image(image,location):
    screen.blit(image,location)

def init():
    winsize = screenwidth,screenheight
    pygame.init()

    global screen
    screen = pygame.display.set_mode()
    screen.convert()
    screen.fill(colors("black"))

#     global background
#     background = pygame.Surface(screen.get_size())
#     background.convert()
#     background.fill(colors("black"))

    pygame.mouse.set_visible(False)

def redisplay():
    #     screen.blit(background,(0,0))
    #     pygame.display.flip()
    pygame.display.update()
    screen.fill(colors("black"))
