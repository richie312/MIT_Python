# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:31:14 2018

@author: Aritra
"""

#outstanding_balance=float(input("Enter the oputstanding the balance"))
#Annual_interest_rate=float(input("Enter the annual interest rate"))
#minimum_payment_rate=float(input("Enter the minimum payment rate"))
outstanding_balance = 4800.00
Annual_interest_rate = 0.2
minimum_payment_rate = 0.04
def credit_statement(outstanding_balance,Annual_interest_rate,minimum_payment_rate):
    assert type(outstanding_balance) == float and type(Annual_interest_rate) == float\
               and type(minimum_payment_rate) == float
    NumMonths = 0
    Amount_paid=0
    
    while NumMonths < 12:
        minimum_monthly_payment = round(minimum_payment_rate*outstanding_balance,2)
        Interest_paid = round((Annual_interest_rate/12)*outstanding_balance,2)
        Principal_Paid = minimum_monthly_payment - Interest_paid
        outstanding_balance -= Principal_Paid
        Amount_paid += minimum_monthly_payment
        NumMonths += 1

        print ("Month:", NumMonths)
        print ("Minimum monthly payment:", minimum_monthly_payment)
        print ("Principal Payment", Principal_Paid)
        print ("Remaining balance:", outstanding_balance)
    print ("The overall payment status at the end of 1st year")    
    print ("Total amount paid:",Amount_paid)
    print ("Remaining balance:",outstanding_balance)

credit_statement(outstanding_balance,Annual_interest_rate,minimum_payment_rate)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                       
                       