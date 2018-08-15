#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:35:17 2018

@author: kilingcheung
"""
import pylab as plt

def ex1(overlay=True):

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
        plt.ylim(0,1000)
        plt.plot(mySamples, myLinear)
        
        plt.figure('quad')
        plt.clf()
        plt.ylim(0,1000)
        plt.plot(mySamples, myQuadratic)
        
        plt.figure('cubic')
        plt.clf()
        plt.plot(mySamples, myCubic)
        
        plt.figure('exp')
        plt.plot(mySamples, myExponential)
        
        plt.figure('quad')
        plt.ylabel('quadratic function')
        
def ex2():
    plt.figure('lin quad')
    plt.clf()
    plt.plot(mySamples, myLinear, label='linear')
    plt.plot(mySamples, myQuadratic, label='quadratic')
    plt.legend(loc = 'upper left')
    plt.title('Linear vs. Quadratic')
    
    plt.figure('cube exp')
    plt.clf()
    plt.plot(mySamples, myCubic, label='cubic')
    plt.plot(mySamples, myExponential, label='exponential')
    plt.legend()
    plt.title('Cubic vs. Exponential')
    
def ex3():
    plt.figure('lin quad')
    plt.clf()
    plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
    plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0)
    plt.legend(loc = 'upper left')
    plt.title('Linear vs. Quadratic')
    
    plt.figure('cube exp')
    plt.clf()
    plt.plot(mySamples, myCubic, 'g^', label='cubic')
    plt.plot(mySamples, myExponential, 'r--', label='exponential')
    plt.legend()
    plt.title('Cubic vs. Exponential')
    
def ex3(logScale=True):
    # add subplot
    plt.figure('lin quad')
    plt.clf()
    plt.subplot(211)
    plt.ylim(0,900)
    plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
    plt.subplot(212)
    plt.ylim(0,900)
    plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0)
    

    plt.figure('cube exp linear')
    plt.legend(loc = 'upper left')
    plt.title('Linear vs. Quadratic')
    plt.clf()
    plt.subplot(121)
    plt.ylim(0, 140000)
    plt.plot(mySamples, myCubic, 'g^', label='cubic')
    plt.subplot(122)
    plt.ylim(0, 140000)
    plt.plot(mySamples, myExponential, 'r--', label='exponential')
    plt.itle('Cubic vs. exponential in linear')
    plt.legend()
    
def ex4(logScale = True):
    # display y-axis in log scale
    plt.figure('lin quad')
    plt.clf()
    plt.ylim(0,900)
    plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
    plt.ylim(0,900)
    plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0)
    
    if (logScale):
        plt.figure('cube exp log')
    else:
        plt.igure('cube exp linear')
    plt.legend(loc = 'upper left')
    plt.title('Linear vs. Quadratic')
    plt.clf()
    plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=2.0)
    plt.plot(mySamples, myExponential, 'r--', label='exponential')
    if (logScale):
        plt.yscale('log')
        plt.title('Cubic vs. exponential in log')
    else:
        plt.itle('Cubic vs exponential in linear')
    plt.legend()    
            
def init1():
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
    
    # ex1(False)
    #ex2()
    ex4()
    
init1()