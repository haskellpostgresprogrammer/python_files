import cPickle
import umarutils as u
import numpy as np
import objectdetector as o

cifardir = "/otherdisk2/data/cifar100/"

def savetovwfile(finelabels,coarselabels,data):
    for x in range(len(finelabels)):
        d = data[x]
        fl = finelabels[x]
        cl = coarselabels[x]
        u.appendfile(o.vwtrainline(fl,list(d),1),cifardir+"finedata")
        u.appendfile(o.vwtrainline(cl,list(d),1),cifardir+"coarsedata")
        

def unpickledata():
    filename = cifardir+"cifar-100-python/train"
    return u.readpickle(filename)

# def savetobatches(l):
#     counter = 0
#     for x in l:
#         u.writepickle(x,cifardir+"batch"+str(counter))
#         counter = counter + 1
#         print "saved batch "+str(counter)

# def savelabelbatches(cats,cl,data):
#     for x in cats:
#         batch = []
#         for y in cl:
#             if x == y[1]:
#                 n = y[0]
#                 batch.append(data[n])
#         u.writepickle(batch,cifardir+"coarselabel"+str(x))
        
# def getbatch(num):
#     return u.readpickle(cifardir+"batch"+str(num))

# import sparsecoding
# import time

# def batchiterate():
#     num = np.random.randint(0,500)
#     print "batch "+str(num)
#     batch = u.readpickle(cifardir+"batch"+str(num))
#     noised = batch+np.random.random(batch.shape)*0.008*batch.std()
#     batchnoised = np.hstack((batch,noised))
#     layers = [3072,100,100,100,100,100,100,100,100,100]
#     try:
#         bestscore = u.readpickle(cifardir+"bestscore")
#     except:
#         bestscore = 1000000000        
#     bestnet = []
#     for z in range(100):
#         net = sparsecoding.autoencoder(layers)
#         for x in batchnoised:
#             y = np.array_split(x,2)
#             denoised = net[1].activate(net[0].activate(y[1]))
#             diff = np.sum(np.abs(y[0]-denoised))/np.sum(y[0])
#             if diff < bestscore:
#                 bestscore = diff
#                 bestnet = net
#                 u.writepickle(bestnet,cifardir+"bestnet")
#                 u.writepickle(bestscore,cifardir+"bestscore")
#                 u.appendfile(str(time.time())+"\n",cifardir+"timelog")
#                 print "score "+str(diff)+",bestscore "+str(bestscore)+",batch "+str(num)
#                 print "found better net"
#         del(net)

# def batchesiterate():
#     for x in range(10000):
#         batchiterate()

# from PIL import Image
# from PIL import ImageOps
# from matplotlib import pyplot as plt

# def grayarr(imagepath):
#     img = Image.open(imagepath)
#     img = ImageOps.grayscale(img)
#     a = np.asarray(img)
#     return a

# def showarray(a):
#     plt.imshow(a)
#     plt.show()

# def batchnet():
#     batch = u.readpickle(cifardir+"batch"+str(np.random.randint(0,
#                                                                 500)))
#     net = u.readpickle(cifardir+"bestnet")
#     return [batch,net]

# def showresult(batchnet):
#     batch = batchnet[0]
#     net = batchnet[1]
#     img = batch[np.random.randint(0,100)]
#     noised = img+np.random.random(img.shape)*0.008*img.std()    
#     denoised = net[1].activate(net[0].activate(img))    
#     all = np.hstack((img,noised,denoised))
#     allsplit = np.hsplit(all,9)
#     imgs = []
#     for x in allsplit:
#         imgs.append(x.reshape((32,32)))
#     i = np.dstack((imgs[0],imgs[1],imgs[2]))
#     n = np.dstack((imgs[3],imgs[4],imgs[5]))
#     d = np.dstack((imgs[6],imgs[7],imgs[8]))
#     showarray(np.hstack((i,n,d)))

# def latestbestnet():
#     log = np.asarray([float(x)
#                       for x in u.readfilenn(cifardir+"timelog")])
#     times = list(log)
#     print "best net found ",str((time.time()-times[-1])/60/60)[:4]," hours ago"
#     xaxis = np.arange(0,log.size)
#     plt.plot(log,xaxis)
#     plt.show()
