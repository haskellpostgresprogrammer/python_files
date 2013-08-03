import umarutils as u
import html as h
import consulting as c
import Image
import ImageDraw
import povray as pv

centerx = 5
centery = 0
centerz = 5
bikelength = 1
bikewidth = 0.5
bikeframeheight = 0.3
seatlength = 0.3
seatbacklength = 0.5
seatwidth = 0.1
bikeframecolor = "Grey"

def bikeframe():
    return [
        pv.box([centerx-(bikelength/2),centery,
                centerz-(bikewidth/2)],
               [centerx+(bikelength/2),
                centery+bikeframeheight,
                centerz+(bikewidth/2)],
               bikeframecolor)        
        ]
def bikeseat():
    return [
        pv.box([5.95,0.25,4.75],
               [6,0.75,5.25],
               "Grey"),
        pv.box([5.7,0.2,4.75],
               [6,0.25,5.25],
               "Grey"),       
        ]

def povfile():
    return [
        pv.incfiles(),
#         pv.skysphere(),
#         pv.plane("y",0,"White"),
        bikeframe(),
        bikeseat(),
        pv.box([0,0,0],[10,2,10],"Grey"),
        pv.camera([4,1,3],[5,0.5,5]),
        pv.lightsource([5,1.9,5],"White"),
        ]

wdir = "/home/umar/public_html/"
# def drawimage():
#     im = Image.new("RGB",(320,240),"lightblue")
#     draw = ImageDraw.Draw(im)
#     draw.arc((10,10,230,230),0,180,fill="green")
#     im.save(wdir+"fh1.png")
#     return

def css():
    return u.flattentostring(h.cssrules([
        ["body","color","black"]
        ]))

def html():
    return [
        h.h1("""The Exerputer
        """),
        h.img("exerputer.png"),
        ]

def run():
    pv.runpov(povfile(),"exerputer")
#     drawimage()
    c.writefile(html(),css())
# run()
