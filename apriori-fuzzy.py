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
    _itemSet = set()
    #_itemSet would be a set of sets.It would contain those sets from the subsetList which surpass minsupport.
    for x in subsetList:
        support = calSupport(x)
        if support >= minSupport:
            _itemSet.add(x)

    return _itemSet

def joinSet(currentLSet,length):
    """Join a set with itself and returns the n-element itemsets""" 
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length]) 



def runApriori(minSupport,num):

    l = set()
    #l is a set of sets. It contains sets of individiual attributes({1},{2},{3},etc.).C1 accd.to apriori.
    
    for i in range(1,num):
        l.add(set([i]))
    
    largeSet=dict()
   # largeSet is a dictionary to store all frequent itemsets, later on used to calculate rules.
    
    oneCSet = returnItemsWithMinSupport(l,minSupport)
    # set of sets containing frequent itemsets of length 1. L1 accd. to apiori.

    currentLSet = oneCSet
    k = 2

    while(currentLSet != set([])):
        largeSet[k-1] = currentLSet
        currentLSet = joinSet(currentLSet, k)
        currentCSet = returnItemsWithMinSupport(currentLSet,minSupport)
        currentLSet = currentCSet
        k = k + 1


    
    # Furthur work on Calculating Confidence
    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), calSupport(item))
                           for item in value])

    toRetRules = []
    for key, value in largeSet.items()[1:]:
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element) 
                if len(remain) > 0:  #change condition to len(remain)=0 if we want only single element on right side rules.or change remain=num if we want for lst element only.)
                    confidence = calSupport(item)/calSupport(element)
                    if confidence >= minConfidence:
                        toRetRules.append(((tuple(element), tuple(remain)),
                                           confidence))
    return toRetItems, toRetRules

