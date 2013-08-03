# import pygame
# import pygamefunctions as p

# p.init()

# done = False
# while not done:

#     p.text("Image Labeler",50,"red",(100,100))

#     p.redisplay()
    
#     events = pygame.event.get( )
#     for e in events:
#         if(e.type == pygame.KEYDOWN):
#             if (e.key == pygame.K_ESCAPE):
#                 done = True
#             elif (e.key == pygame.K_q):
#                 done = True

from Tkinter import *
import tkFont
from PIL import Image, ImageTk

def main():
    root = Tk()

    customfont = tkFont.Font(family="Arial",size=30)

    image = Image.open("/home/umar/public_html/one.jpg")
    photo = ImageTk.PhotoImage(image)
    imagesize = image.size

    imagearea = Canvas(root)
    imagewidth = imagesize[0]
    imageheight = imagesize[1]
    imagearea.config(width=imagewidth,
                     height=imageheight)
    imagearea.pack()
    #     drawing_area.bind("<Motion>", motion)
    imagearea.bind("<Button-1>", b1down)
    #     drawing_area.bind("<ButtonRelease-1>", b1up)
    imagearea.create_image(0,0,anchor=NW,
                           image=photo)

    labelsframe = Frame(root)
    
    backgroundbutton = Button(labelsframe,
                              text="background",
                              fg="red",
                              command=backroundb,
                              font=customfont)
    backgroundbutton.pack(side=LEFT)

    foregroundbutton = Button(labelsframe,
                              text="foreground",
                              fg="green",
                              command=foregroundb,
                              font=customfont)
    foregroundbutton.pack(side=RIGHT)

    appframe = Frame(root)

    quitbutton = Button(appframe,
                        text="quit",
                        fg="black",
                        command=quitb,
                        font=customfont)
    quitbutton.pack(side=BOTTOM)

    classifybutton = Button(appframe,
                        text="classify",
                        fg="blue",
                        command=classifyb,
                        font=customfont)
    classifybutton.pack(side=TOP)

    labelsframe.pack()
    appframe.pack(side=BOTTOM)

    root.mainloop()

foreground = True

labels = []

def backroundb():
    global foreground
    foreground = False
def foregroundb():
    global foreground
    foreground = True
def quitb():
    print labels
    quit()
def classifyb():
    print "classify"

def b1down(event):
    global labels
    if foreground == True:
        fillcolor = "green"
        labels.append(["foreground",event.x,event.y])
        print "foreground:",event.x,":",event.y
    else:
        fillcolor = "red"
        labels.append(["background",event.x,event.y])
        print "background:",event.x,":",event.y

    event.widget.create_rectangle(event.x-5,
                                  event.y-5,
                                  event.x+5,
                                  event.y+5,
                                  fill=fillcolor)


main()
