# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 19:31:35 2018

@author: Richie
"""

def factorial(n):
    if n == 0:
        return 1
    
def factorial(n):
        if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    
factorial(3)