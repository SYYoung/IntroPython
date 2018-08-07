#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 23:07:41 2018

@author: kilingcheung
"""

def isPrime(num):
    if (num == 2):
        return True
    elif (num %2 == 0):
        return False
    else:
        for i in range(3,num-1):
            if (num % i == 0):
                return False
        return True
    
def getPrimes():
    num = 2
    while True:
        if isPrime(num):
            yield num
        num += 1
        
def genPrimes():
    p = []
    x = 2
    isPrime = True
    while True:
        for known in p:
            if (x % known == 0):
                isPrime = False
                break
            else:
                isPrime = True
        if (isPrime):
            p.append(x)
            yield x
        x += 1