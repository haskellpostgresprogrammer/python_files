import umarutils as u

# import cv

# capture = cv.CaptureFromFile('skyline.mov')
# frames = []
# for i in range(100):
#     img = cv.QueryFrame(capture)
#     tmp = cv.CreateImage(cv.GetSize(img),8,3)
#     cv.CvtColor(img,tmp,cv.CV_BGR2RGB)
#     frames.append(asarray(cv.GetMat(tmp))) 
# frames = array(frames)

# total frames count
# ffmpeg -i obamaspeech.mp4 -an -vcodec copy -f mp4 -y /dev/null

# def videoinfo():
#     return u.shellcommand(
#         ["ffmpeg",
#          "-i","/otherdisk2/data/obamaspeech/obamaspeech.mp4",
#          "-an","-vcodec","copy",
#          "-f","mp4","-y","/dev/null"])

# mencoder -nosound -ovc frameno -vc null -o /dev/null obamaspeech.mp4

# mplayer obamaspeech.mp4 -nosound -vc null -vo null -benchmark -nocorrect-pts

# mplayer -vo jpeg -frames 1 -ss 5 obamaspeech.mp4

# get frame
# ffmpeg -vframes 1 -ss 6.2 -i obamaspeech.mp4 oneframe.jpg

def videoinfo(filename):
    a = u.shellcommand(
        ["mplayer",filename,
         "-nosound","-vc","null",
         "-vo","null","-benchmark",
         "-nocorrect-pts"])
    b = a.split("\n")
    c = [x.split("\r") for x in b]
    d = c[20][-2].split(" ")
    return d

def videoframes(filename):
    return int(videoinfo(filename)[2].split("/")[1])

def videolength(filename):
    return float(videoinfo(filename)[1])

def getframe(start,video,image):
    return u.shellcommand(
        ["ffmpeg","-vframes","1","-ss",str(start),
         "-i",video,image])

import Tkinter as Tkinter
from PIL import ImageTk, Image                        

def displayimage(image_pil):
    root = Tkinter.Tk()
    drawing_area = Tkinter.Canvas(root)
    drawing_area.config(width=800,height=600)
    drawing_area.pack()
    i = ImageTk.PhotoImage(image_pil)
    drawing_area.create_image(0, 0, image=i)
    root.mainloop()

def getimage(filename):
    return Image.open(filename)

def getimagesize(pil_image):
    return pil_image.size

obdir = "/otherdisk2/data/obamaspeech/"
svdir = "/otherdisk/myfiles/videos/shortvideos/"
obv = obdir+"obamaspeech.mp4"
svv = svdir+"We_got_scared-Ela3ChTzFcA.mp4"
imgname = "one.jpg"
outimg = obdir+imgname
homedir = "/home/umar/"
localwebdir = homedir+"public_html/"

def ex():
    return getframe(10,obv,outimg)
def ex2():
    return  getframe(10,svv,outimg)
def getandcopyframe():
    ex()
    return u.shellcommand(
        ["cp",outimg,localwebdir])
