#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:07:46 2018

@author: r38411
"""
def fun1():
    s = "abcdefgh"
    startInd = 0
    #endInd = 0
    total = 1
    #result = s[0]
    curTotal = 1
    for i in range(1,len(s)):
        if s[i-1] <= s[i]:
            #endInd = i
            curTotal = curTotal + 1
        else:
            if (curTotal > total):
                total = curTotal
                result = s[startInd:i]
            curTotal = 1
            startInd = i
            endInd = i
    if (curTotal == len(s)):
        result = s
    print("Longest substring in alphabetical order is: " + result)
    
    while (True):
        x = int(input("Please think of a number between 0 and 100!"))
        low = 0
        high = 100
        ans = (low + high)/2
        
    def is_even(i):
        """
        Input: i, a positive int
         Returns True if i is even, otherwise False
        """
        return(i%2==0)     
        
def isIn(char, aStr):
    # test the middle char
    if (char == aStr[len(aStr)//2]):
        return True
    elif (len(aStr) == 1):
        return False
    elif (not aStr):
        return False
    elif (char < aStr[len(aStr)//2]):
        return isIn(char, aStr[:len(aStr)//2])
    else:
        return isIn(char, aStr[len(aStr)//2 +1:])
    
#theChar = 'm'
#theStr = 'abcdlmno'
#_4result = isIn(theChar, theStr)

def debtPayOff1(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12.0
    minMonthlyPay = 0
    nextBal = balance
    while (nextBal > 0):
        minMonthlyPay += 10
        curBal = balance
        nextBal = balance
        numMonth = 0
        #print("monthly payment : " + str(minMonthlyPay))
        while (numMonth <= 11):
            curBal = nextBal
            unpaidMonthlyBal = curBal - minMonthlyPay
            nextBal = unpaidMonthlyBal + (monthlyInterestRate * unpaidMonthlyBal)
            numMonth += 1
        #print("by end of Month 12, remaining balance: " + str(round(nextBal,2)))
    print("Lowest Payment: " + str(minMonthlyPay))    
    
def debtPayOff2(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12.0
    lower = balance/12
    upper = (balance * (1+monthlyInterestRate)**12)/12.0
    nextBal = balance
    spare = 0.0
    while (nextBal > 0):
        minMonthlyPay = (lower + upper)/2
        curBal = balance
        nextBal = balance
        numMonth = 0
        #print("monthly payment : " + str(minMonthlyPay))
        while (numMonth <= 11) and (nextBal > 0):
            curBal = nextBal
            unpaidMonthlyBal = curBal - minMonthlyPay
            nextBal = unpaidMonthlyBal + (monthlyInterestRate * unpaidMonthlyBal)
            numMonth += 1
        #print("by end of Month 12, remaining balance: " + str(round(nextBal,2)))
        if (numMonth >= 12) and (nextBal >0):
            lower = minMonthlyPay
        elif (numMonth <=11) and (nextBal < 0):
            upper = minMonthlyPay
        elif (numMonth == 12) and (nextBal < -0.05):
            upper = minMonthlyPay
        else:
            break
        nextBal = balance
    print("Lowest Payment: " + str(round(minMonthlyPay,2))) 
    #return minMonthlyPay
    
balance = 999999
annualInterestRate = 0.18
debtPayOff2(balance, annualInterestRate)