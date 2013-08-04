import numpy as np
import os
from matplotlib import pyplot as plt

def showarray(a):
    plt.imshow(a)
    plt.show()

# def grayarr(imagepath):
#     img = Image.open(imagepath)
#     img = ImageOps.grayscale(img)
#     a = np.asarray(img)
#     return a

# def featurize(data,amount):
#     outered = np.outer(data,data)
#     flattened = outered.flatten()
#     repeated = np.repeat(flattened,amount)
#     r = np.random.random(amount)
#     print outered.shape
#     print flattened.shape
#     print repeated.shape
# def test():
#     a = featurize(np.random.random(1000),20)
    
def splotches2d(x,y,z,n):
    r = np.sum(np.random.randint(0,2,(x,y*n,z)),2)
    rbinned = np.reshape(np.digitize(r.flatten(),[0,1]),
                         (x,y*n))-np.ones((x,y*n))
    return rbinned

def randomfeaturevector2d(x,y,n):
    multiplier = np.random.random((x,y*n)).flatten()
    splotches = splotches2d(x,y,3,n).flatten()
    return np.hstack((multiplier,splotches))

def train2d(labels,data,x,y,n):
    datan = np.tile(data,n*2)
    r = randomfeaturevector2d(x,y,n)
    rr = np.repeat(r,
                   labels.size).reshape((labels.size,x*y*n*2))
    dr = datan*rr
    model = np.linalg.lstsq(dr,np.reshape(labels,(labels.size,1)))
    return [model,r]

def test():
    return train2d(np.random.randint(0,2,500),
                   np.random.random((500,32*32)),
                   32,32,10)
