# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:28:57 2015

@author: zhyfly711
"""

'''Implicit graph search and maximal cliques'''

class puzzle(object):
    def __init__(self, order):
        self.label = order
        for index in range(9):
            if order[index] == '0':
                self.spot = index
                return None
    '''tansition just generate a new label with the desired location of blank'''
    def transition(self, to): # 'to' is a location to do a shift
        label = self.lable
        blankLocation = self.spot
        newBlankLabel = str(label[to])
        newLabel = ''
        for i in range(9):
            if i == to:
                newLabel += '0'
            elif i == blankLocation:
                newLabel += newBlankLabel
            else:
                newLabel += str(label[i])
        return puzzle(newLabel)
    
    def __str__(self):
        return self.label

'''set up a dict with values mean which can move to the index
look at the class notes'''
shiftDict = {}
shiftDict[0] = [1, 3]
shiftDict[1] = [0, 2, 4]
shiftDict[2] = [1, 5]
shiftDict[3] = [0, 4, 6]
shiftDict[4] = [1, 3, 5, 7]
shiftDict[5] = [2, 4, 8]
shiftDict[6] = [3, 7]
shiftDict[7] = [4, 6, 8]
shiftDict[8] = [5, 7]

'''breadth first search with generator, b/c it will generate the nodes'''
def BFSWithGenerator(start, end, q = []):
    initPath = [start]
    q.append(initPath)
    while len(q) != 0:
        tempPath = q.pop(0)
        lastNode = tempPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift)
            if not:
                
                



'''maximal clique'''
'''(1) generating a power set recursively. How? Find the power set of all but
   first element. then compy each element of that set, with first element added,
   finally combine both sets as answer.'''
def powerSet(elts):
    if len(elts) == 0:
        return [[]]
    else:
        smaller = powerSet(elts[1:])
        elt = [elts[0]]
        withElt = []
        for s in smaller:
            withElt.append(s + elt)
        allofthem = smaller + withElt
        return allofthem
        
'''(2)Generate the power set of all the nodes in the graph'''
def powerGraph(gr):
    nodes = gr.nodes
    nodesList = []
    for elt in nodes:
        nodesList.append(elt)
    pSet = powerSet(nodesList)
    return pSet

'''(3)test if a set is a clique'''
def allConnected(gr, candidate):
    for n in candidate:
        for m in candidate:
            if n not in gr.childrenOf(m):
                return False
    return True

'''(4)Find the biggest clique in the graph'''
def maxClique(gr):
    candidates = powerGraph(gr)
    keepEm = []
    for candidate in candidates:
        if allConnected(gr, candidate):
            keepEm.append(candidate)
    bestLength = 0
    bestSoln = None
    for test in keepEm:
        if len(test) > bestLength:
            bestLength = len(test)
            bestSoln = test
    return bestSoln



















