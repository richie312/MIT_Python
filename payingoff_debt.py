# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 12:11:27 2018

@author: Aritra
"""

balance = 1200.00
annual_interest_rate = 0.18

    
Minimum_fixed_monthly_payment = 0
monthly_interest_rate = annual_interest_rate/12
outstanding_balance = balance

while outstanding_balance > 0:
    outstanding_balance = balance
    numMonths = 0
    Minimum_fixed_monthly_payment += 10
    while numMonths < 12 and outstanding_balance > 0:
        numMonths += 1 
        interest = outstanding_balance*monthly_interest_rate
        outstanding_balance -= Minimum_fixed_monthly_payment
        outstanding_balance += interest
    
outstanding_balance = round(outstanding_balance,2)        
print ("The Fixed monthly payment $ ",Minimum_fixed_monthly_payment)
print ("Required Number of months is ", numMonths)
print ("The remaining balance is $ ", outstanding_balance)

import turtle
for i in range(10):
    turtle.forward(15)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()                                         
                                              
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    