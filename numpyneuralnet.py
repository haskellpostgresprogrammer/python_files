import numpy as np
import scipy.optimize as opt

def ex(a):
    return np.absolute(np.sum(a))

def findmin():
    r = np.random.rand(4)
    return opt.fmin(ex,r)

def perceptrontrain():
    inputsize = 4
    numinputs = 10
    bias = 0.0
    initialweights = np.random.rand(inputsize)
    inputdata = np.random.rand(numinputs,inputsize)
    outputdata = np.random.rand(numinputs)
    weighted = np.multiply(inputdata,initialweights)
    summed = np.sum(weighted,1)
    biased = np.subtract(summed,bias)
    errors = np.subract(outputdata,biased)
    totalerror = np.sum(errors)
    return totalerror
