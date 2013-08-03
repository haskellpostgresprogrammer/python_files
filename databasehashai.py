import numpy as np
from matplotlib import pyplot as plt
import umarutils as u

# def showdist():
#     a = np.digitize(np.random.random(100*100),
#                     [0.8]).reshape((100,100))
#     plt.imshow(a)
#     plt.show()
    
# def digitizedata(data,digitizations):
#     maxv = np.max(data)
#     minv = np.min(data)
#     digitizeddatalist = []
#     for x in range(2,digitizations):
#         bins = np.ones(x).cumsum()/x
#         digitizeddatalist.append(np.digitize(data,bins))
#     digitizeddata = np.asarray(digitizeddatalist).flatten()
#     return digitizeddata

# def createselectors(size,number):
#     return np.digitize(np.random.random((size,number)),
#                        [0.9])    

# def selectorize(selectors,data,digitizations):
#     return selectors*digitizedata(data,digitizations)

def createrandomprojections(amount,size,file):
    u.writepickle(file,np.random.random((amount*size)))
    print "written random projections in ",file

# def createrandomcuts(amount,size,file):
#     u.writepickle(file,np.random.randint(0,2,(amount*size)))
#     print "written random cuts in ",file

def randomprojectiondigitizehash(data,,
                                 randomprojections,
                                 digitizations):
    projection = np.repeat(data,randomprojection.size/data.size)*randomprojections
    maxv = np.max(projection)
    minv = np.min(projection)
    digitizationslist = []
    for x in range(2,digitizations):
        bins = np.ones(x).cumsum()/x
        digitization = np.digitize(projection,bins)
        digitizationslist.append(digitization)
    return digitizationslist

def saveprojectionhashes(data,label,randomprojections,
                         digitizations,directory):
    for x in randomprojectiondigitizehash(data,
                                          randomprojections,
                                          digitizations):
        u.writefile(label,directory+str(hash(x)))

def matchprojections(data,randomprojections,digitizations,
                     directory):
    labels = []
    for x in randomprojectiondigitizehash(data,
                                          randomprojections,
                                          digitizations):
        labels.append(u.readfile(directory+str(hash(x))))
    return labels
