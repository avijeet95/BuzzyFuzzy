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

def joinSet(currentLSet,length):
    pass


def runApriori(minSupport,num):

    l = []
    
    for i in range(1,num):
        l.append([i])
    
    oneCSet = returnItemsWithMinSupport(l,minSupport)

    currentLSet = oneCSet
    k = 2

    while(currentLSet != list([])):
        largeSet[k-1] = currentLSet
        currentLSet = joinSet(currentLSet, k)
        currentCSet = returnItemsWithMinSupport(currentLSet,minSupport)
        currentLSet = currentCSet
        k = k + 1


    #MAKE JOINSET function
    # Furthur work on Calculating Confidence


