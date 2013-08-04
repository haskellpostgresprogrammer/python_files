from pyfann import libfann

def network(inputsize,h1,h2,h3,h4,h5,h6,outputsize):
    connect_rate = 0.1
    ann = libfann.neural_net()
    ann.create_sparse_array(connect_rate,
                            (inputsize,
                             h1,h2,h3,h4,h5,h6,
                             outputsize))
    ann.set_activation_function_output(libfann.SIGMOID_SYMMETRIC_STEPWISE)
    return ann

def savenetwork(thefile,network):
    annfile = thefile
    network.save(annfile)

def loadnetwork(thefile,network):
    ann = libfann.neural_net()
    ann.create_from_file(thefile)

def predict(network,inputs):
    network.run(inputs)

def standardnetwork(inputsize,outputsize):
    return network(inputsize,
                   2000,3000,5000,3000,2000,1000,outputsize)

import random
import time
def testnetwork():
    t1 = time.time()
    net = standardnetwork(1000,1000)
    t2 = time.time()
    for x in range(100):
        a = random.random()
        b = random.random()
        predict(net,[a,b])
    t3 = time.time()
    tt1 = t2 - t1
    tt2 = t3 - t2
    return tt1,tt2
