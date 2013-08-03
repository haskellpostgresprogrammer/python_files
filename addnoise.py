from PIL import Image
from PIL import ImageOps
import numpy as np
from matplotlib import pyplot as plt

def grayarr(imagepath):
    img = Image.open(imagepath)
    img = ImageOps.grayscale(img)
    a = np.asarray(img)
    return a
def imgarr(imagepath):
    img = Image.open(imagepath)
    a = np.asarray(img)
    return a
    
def showarray(a):
    plt.imshow(a)
    plt.show()

def addnoise(a,amount):
    #     noisedpath = "".join([imagepath.rsplit("/",1)[0],
    #                           "/noise",
    #                           imagepath.rsplit("/",1)[1]])
    #     a = grayarr(imagepath)
    r = np.random.random(a.shape)*amount*a.std()
    b = a+r
    #     img = Image.fromarray(b)    
    #     img.save(noisedpath)
    #     plt.imshow(b, interpolation='nearest')
    return [a,b]

# def noisetest():
#     a = addnoise("/home/umar/dog.jpg",10)
#     showarray(np.vstack((a[0],a[1])))

def noisemeasure(data,noisedata):
    diff = np.sum(np.abs(data-noisedata))
    datatotal = np.sum(data)
    return diff/datatotal

# def noisemeasuretest():
#     a = addnoise("/home/umar/dog.jpg",25)
#     b = noisemeasure(a[0],a[1])
#     return b
