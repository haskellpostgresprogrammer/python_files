import pybrain
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet    
from pybrain.supervised.trainers import BackpropTrainer
import random
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection

layer1 = 100
layer2 = 100
layer3 = 100
layer4 = 100
trainingepochs = 50

def logisticregressor(insize):
    return buildNetwork(insize,1)
def ffnet(sizes):
    return apply(buildNetwork,sizes)
# def rnet(sizes):
#     return apply(buildNetwork,sizes,recurrent=True,fast=True])

def trainlogisticregression(net,dataset,loops):
    trainer = BackpropTrainer(net,dataset)
    for x in range(loops):
        trainer.train()
    return net
def logisticdataobject(insize):
    ds = SupervisedDataSet(insize,1)
    return ds

def buildfeaturizer():
    return buildNetwork(layer1,layer2,layer3,layer4)
def buildlearner():
    return buildNetwork(layer4,1,1)

def createdataset(indata,outdata):
    ds = SupervisedDataSet(layer4,1)
    for x,y in indata,outdata:
        ds.addSample(x,y)
    return ds

def datasetobject():
    ds = SupervisedDataSet(layer4,1)
    return ds

def predict(net,data):
    return net.activate(data)

def trainnetwork(net,dataset):
    trainer = BackpropTrainer(net,dataset)
    for x in range(trainingepochs):
        trainer.train()
    return net

def learnertest():
    numrange = range(100)
    samples = 100
    zeroes = [0 for x in range(samples)]
    ones = [1 for x in range(samples)]
    dataset = datasetobject()
    for sample in range(samples):
        c = random.choice([0,1])
        if c == 0:
            dataset.addSample(zeroes,0)
        elif c == 1:
            dataset.addSample(ones,1)
    net = buildlearner()
    print "training"
    trainednet = trainnetwork(net,dataset)
    print "predicting"
    predictions = []
    for x in range(10):
        c = random.choice([0,1])
        if c == 0:
            predictions.append([0,
                                int(round(trainednet.activate(zeroes)[0]))])
        elif c == 1:
            predictions.append([1,
                                int(round(trainednet.activate(ones)[0]))])
    return [predictions,trainednet]

def featurizertest():
    zeroes = [0 for x in range(100)]
    ones = [1 for x in range(100)]
    net = buildfeaturizer()
    return [list(net.activate(zeroes)),list(net.activate(ones))]

def autoencode(data,codelayers,decodelayers):
    codenet = ffnet(codelayers)
    decodenet = ffnet(decodelayers)
    codeddata = codenet.activate(data)
    decodeddata = outnet.activate(codeddata)
    return [codenet,decodenet,decodeddata]

# import conkeror
# from PIL import Image
# from PIL import ImageOps
# import numpy as np
# import scipy

# def noise(imagepath):
#     noisedpath = "".join([imagepath.rsplit("/",1)[0],
#                           "/noise",
#                           imagepath.rsplit("/",1)[1]])

#     img = Image.open(imagepath)
#     img = ImageOps.grayscale(img)

#     a = numpy.asarray(img)
#     r = numpy.random.randint(0,3,a.shape)
#     b = a*3

#     img = Image.fromarray(b)    
#     img.save(noisedpath)
# #     conkeror.conkeroropen(noisedpath)


# def randomfeatures(data,randomizersize):
#     datacrossproduct = numpy.cross(data,data)
#     randomizer = numpy.random.random(data,randomizersize)        
#     return numpy.cross(datacrossproduct,randomizer)
# # follow with linear regression
# # use noise -> denoise high throughput for
# # sparse coding (lots of unlabelled data)

# # to download imagenet urls
# # cat *.urls | grep flickr >flickrdowns (to avoid name clashes)
# # wget -i flickrdowns -nc -T 2 -retry 0
