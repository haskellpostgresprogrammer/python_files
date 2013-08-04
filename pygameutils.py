import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import os
import time

def initialize():
    # Initialise screen
    global pygame
    pygame.init()

    global screen
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Life Management')    

    global background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

def selectcolor(color):
    return THECOLORS[color]

def fillbackground(color):
    global background
    background.fill(selectcolor(color))
# def fillbackgroundred():
#     background.fill(THECOLORS["red"])

def redisplay():
    screen.blit(background, (0, 0))
    pygame.display.flip()

def display(object,position):
    background.blit(object,position)

def getevents():
    return pygame.event.get()

# sound
# def sound(path):
#     return pygame.mixer.Sound(os.path.join(*path))

# nosound = sound(["/usr","share","gcompris","boards","sounds",
#                  "memory","tri.ogg"])
# yessound = sound(["/usr","share","gcompris","boards","sounds",
#                   "memory","plick.ogg"])
# classifysound = sound(["/usr","share","gcompris","boards","sounds",
#                        "memory","tick.ogg"])
# erasesound = sound(["/usr","share","assetml","childsplay",
#                     "sounds-misc","slideup.ogg"])

# image
# imagefile = os.path.join("/home","umar","dog.jpg")
# image = pygame.image.load(imagefile)
# image = image.convert()
# imagetopleft = (200,200)
# def displayimage():
#     display(image,imagetopleft)

def drawtext(text,size,location,color):
    font = pygame.font.Font(None,size)
    display(font.render(text,1,THECOLORS[color]),location)

def textsize(text,size):
    font = pygame.font.Font(None,size)
    return font.size(text)

# def quitevent(e):
#     if e.type == QUIT:
#         exit()
# def escapekey(e):
#     if e.key == K_ESCAPE:
#         exit()
#     if e.key == K_q:
#         exit()
# def keydown(e):
#     if e.type == KEYDOWN:
#         escapekey(e)    


