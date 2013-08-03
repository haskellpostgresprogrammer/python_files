import pybrain
from pybrain.tools.shortcuts import buildNetwork

# def createnetwork(input,hiddenlayers,output):
#     from pybrain.tools.shortcuts import buildNetwork
#     net = buildNetwork(input,hiddenlayers,output)
#     return net

# def createdataset(insize,outsize,indata,outdata):
#     from pybrain.datasets import SupervisedDataSet    
#     ds = SupervisedDataSet(insize,outsize)
#     for x,y in indata,outdata:
#         ds.addSample(x,y)
#     return ds

# def trainnetwork(network,dataset):
#     from pybrain.supervised.trainers import BackpropTrainer
#     trainer = BackpropTrainer(network,dataset)
#     #trainer.train()
#     trainer.trainUntilConvergence()
#     return network

# def doneuralnetwork(insize,hiddensize,outsize,indata,outdata):
#     net = createnetwork(insize,hiddensize,outsize)
#     data = createdataset(insize,outsize,indata,outdata)
#     trainednet = trainnetwork(net,data)
#     return trainednet

# def predict(network,data):
#     return network.activate(data)

# net.activate((2, 3))
# array([ 0.6656323,  0.3343677])

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer,SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet    
from pybrain.supervised.trainers import BackpropTrainer

def encoderdecoder(outersize,innersize,indata,
                   fname):
    # create network
    n = FeedForwardNetwork()

    inLayer = LinearLayer(outersize)
    hiddenLayer = SigmoidLayer(innersize)
    outLayer = LinearLayer(outersize)

    n.addInputModule(inLayer)
    n.addModule(hiddenLayer)
    n.addOutputModule(outLayer)

    in_to_hidden = FullConnection(inLayer, hiddenLayer)
    hidden_to_out = FullConnection(hiddenLayer, outLayer)
    n.addConnection(in_to_hidden)
    n.addConnection(hidden_to_out)

    n.sortModules()
    
    # create dataset
    ds = SupervisedDataSet(outersize,outersize)
    for x,y in indata,indata:
        ds.addSample(x,y)

    # train network
    trainer = BackpropTrainer(n,ds)
    trainer.trainUntilConvergence()

    n.saveNetwork(fname)
    
    return [[in_to_hidden,hidden_to_out],
            [inLayer,hiddenLayer,outLayer],
            n]
