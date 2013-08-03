import numpy as np

def randomfeaturize(data,size):
    return np.repeat(data.flatten(),size)-np.random.random(data.size*size)

def datafeaturize(data,exampledata):
    return  np.repeat(data.flatten(),exampledata.size)-exampledata.flatten()

# vipscc - images too large to fit in memory - can use that to find
# diff with larger number of example images
