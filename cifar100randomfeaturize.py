import numpy as np
import vowpalwabbit as vw
import cifar100
import umarutils as u

def makefile(data,labels,labelname):
    num = 0
    for y in range(50000/500):
        chunk = []
        for z in range(500):
            d = list(data[num])
            l = labels[num]
            label = str(l)+" | "
            features = " ".join([str(x[0])+":"+str(x[1])
                                 for x in zip(range(len(d)),d)])
            chunk.append(label+features)
            num = num + 1
        u.appendfile("\n".join(chunk),
                     cifar100.cifardir+"vwtraindata"+labelname)
