#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:35:17 2018

@author: kilingcheung
"""
import pylab as plt

def ex1(overlay=True):
    mySamples = []
    myLinear = []
    myQuadratic = []
    myCubic = []
    myExponential = []
    
    for i in range(0,30):
        mySamples.append(i)
        myLinear.append(i)
        myQuadratic.append(i**2)
        myCubic.append(i**3)
        myExponential.append(1.5**i)
    if overlay :    
        plt.plot(mySamples, myLinear)
        plt.plot(mySamples, myQuadratic)
        plt.plot(mySamples, myCubic)
        plt.plot(mySamples, myExponential)
    else:
        plt.figure('lin')
        plt.clf()
        plt.xlabel('sample points')
        plt.ylabel('linear function')
        plt.plot(mySamples, myLinear)
        
        plt.figure('quad')
        plt.clf()
        plt.plot(mySamples, myQuadratic)
        
        plt.figure('cubic')
        plt.clf()
        plt.plot(mySamples, myCubic)
        
        plt.figure('exp')
        plt.plot(mySamples, myExponential)
        
        plt.figure('quad')
        plt.ylabel('quadratic function')
        
        