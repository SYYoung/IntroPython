#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 17:28:43 2018

@author: r38411
"""

def getLongSubStr(s1):
    result = s1[0]
    tmp = [s1[0]]
    for i in range(1, len(s1)):
        if (s1[i] >= tmp[-1]):
            tmp.append(s1[i])
        else:
            if (len(tmp) > len(result)):
                result = tmp[:]
            tmp = [s1[i]]
    print(result)
    print(''.join(result))
    return ''.join(result)
        
    
#s = 'cdeababcdefgcb'
s = 'wb'
getLongSubStr(s)