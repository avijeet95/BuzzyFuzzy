import sys
import test

from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser
import numpy as np
from sets import Set

attribute = np.matrix('1 2 -1; 4 5 -3')

def calSupport(itemSet):
    
    data = []
    totalSum = 0
    # tempList =[]

    for x in itemSet:
        tempList = np.array(attribute[0: , x])
        data.append(tempList)

    data = np.array(data)


    minData = np.amin(data,axis = 1)
    
    for x in minData:
        totalSum+=x
    return totalSum



def returnItemsWithMinSupport(subsetList,minSupport):
    _itemSet = []
    for x in subsetList:
        support = calSupport(x)
        if support >= minSupport:
            _itemSet.append(x)

    return _itemSet


#Testing Function
print returnItemsWithMinSupport([[0,1],[0,2]] , -100)

