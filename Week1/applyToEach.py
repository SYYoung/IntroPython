# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 19:24:14 2016

@author: ericgrimson
"""

def applyToEach(L, f):
    """assumes L is a list, f a function
       mutates L by replacing each element,
       e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])
        

def applyFuns(L, x):
    for f in L:
         print(f(x))

def uni(aDict):
    valL = []
    for i in aDict:
        valL.append(aDict[i])
    keyL = []
    for i in aDict:
        if (valL.count(aDict[i]) == 1):
            keyL.append(i)
    if (len(keyL) > 0):
        keyL.sort()
    return keyL

def getElem(t):
    valL = []
    for item in t:
        if (isinstance(item, tuple) or isinstance(item, list)):
            valL.extend(getElem(item))
        else:
            valL.append(item)
    return valL
    
    
def max_val(t):
    newL = getElem(t)
    return max(newL)

def satisfiesF(L):
    newL = L[:]
    for i in newL:
        if (not f(i)):
            L.remove(i)
    return len(L)
  
def f(s):
    return 'a' in s

def run_satisfiesF(L, myFunc):
    myFunc(L)
    
#myDict = {'a':1, 'b':2, 'c':3, 'd':1, 'e':5}
#print(uni(myDict))
#myList = ((5, (1,2), [[1],[9]]))
#newL = getElem(myList)
#val = max_val(myList)
myFunc = satisfiesF
L = ['a', 'b', 'a']
run_satisfiesF(L, myFunc)