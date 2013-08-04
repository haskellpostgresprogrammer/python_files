import umarutils as u
import numpy as np
# from PIL import Image
# from PIL import ImageOps
import socket
import subprocess
import time

# def imagetofeaturevector(image,num):
#     data = list(im.getdata())
#     return datatovector()

def vwtrainline(label,data,num):
    datanum = []
    for x in range(num):
        datanum.extend(data)
    vwstring = " |f ".join([str(label),
                           " ".join([str(x[0])+":"+str(x[1])
                                     for x in zip(range(len(data)*num),
                                                  datanum)])])
    return vwstring+"\n"

def vwpredictline(data,num):
    datanum = []
    for x in range(num):
        datanum.extend(data)
    vwstring = "|f ".join(["",
                           " ".join([str(x[0])+":"+str(x[1])
                                     for x in zip(range(len(data)*num),
                                                  datanum)])])
    return vwstring+"\n"

def vwsend(msg):
    vw = socket.socket()
    vw.connect_ex(("localhost",26542))
    sent = vw.send(msg)
#     if sent == 0:
#         raise RuntimeError("connection broken")
    received = vw.recv(100)    
    vw.close()
    return received

def trainvwresume(inregressor,outregressor,passes,datafile):
    subprocess.call(["/home/umar/vw",
                     "-c",#"--compressed",
                     "-i",inregressor,
                     "-f",outregressor,
                     "--passes",str(passes),
                     "-d",datafile])
def trainvwinitial(outregressor,passes,datafile):
    subprocess.call(["/home/umar/vw",
                     "-c",#"--compressed",
                     "-f",outregressor,
                     "--passes",str(passes),
                     "-d",datafile])
def startvwpredictor(inregressor):
    subprocess.call(["/home/umar/vw","--quiet","--daemon",
                     "-c",#"--compressed",
                     "-i",inregressor])
def killvw():
    subprocess.call(["killall","vw"])

def vwpredict(data,num):
    return vwsend(vwpredictline(data,num))

def test():
    data = [[x for y in range(5)] for x in range(10)]
    for x in data:        
        u.appendfile(vwtrainline(x[0],x,10),
                     "/home/umar/testdata1")
    print trainvwinitial("/home/umar/testreg1",3,
                         "/home/umar/testdata1")
    time.sleep(5)
    startvwpredictor("/home/umar/testreg1")
    for x in data:
        time.sleep(2)
        print "predicting ",x[0]," : ",vwpredict(x,10)
    killvw()
    subprocess.call(["rm","/home/umar/testdata1.cache"])
    subprocess.call(["rm","/home/umar/testdata1"])
    subprocess.call(["rm","/home/umar/testreg1"])
