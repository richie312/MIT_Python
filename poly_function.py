# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:33:14 2018

@author: Richie
"""


poly = (0.0,0.0,5.0,9.3,7.0)
x= -13

def evaluate_poly(poly,x):
    total = 0.0
    for i in range(len(poly)):
        total += poly[i]*x**i
        return total
evaluate_poly(poly,x)    

poly1 = (-13.39,0.0,17.5,3.0,1.0)
poly2 = (1,3,17.5,0,-13.39)

for i in range(len(poly)):
    print(poly[i])    


## define function for derivative


def compute_derive(poly):
    poly_derive = []
    if len (poly) < 2:
        return [0,0]
    else:
        for i in range(1,len(poly)):
             poly_derive.append(i*poly[i])
        return poly_derive
compute_derive(poly1)            
            
## Newton Raphson method

epsilon=0.0001
poly = (-13.39,0.0,17.5,3.0,1.0)
x_0 = 0.1
def compute_root(poly,x_0,epsilon):
    root = x_0
    numGuesses = 1
    while abs(evaluate_poly(poly,root))>= epsilon:
            root = (root - evaluate_poly(poly, root) /
                evaluate_poly(compute_derive(poly), root))
            numGuesses += 1
    return [root,numGuesses]
        
compute_root(poly,x_0,epsilon)        



























