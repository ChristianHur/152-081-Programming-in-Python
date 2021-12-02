# -*- coding: utf-8 -*-
"""
RECURSION (Recursive function) - a function that calls itself

Write a program that calculates and displays the conversion of an
entered number of dollars into currency denominations:
100s, 50s, 20s, 10s, 5s, 1s, half-dollars, quarters, dimes, nickles, pennies.

Algorithm:  Using a counter (index)
"""

dollars = float(input("Enter amount:"))

denominations = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
def count_denom( dollars, i ):
    
    if i == len(denominations): return  #DONE
    
    qty = int(dollars // denominations[i])
    
    if denominations[i] >= 1:
        print(f'${str(denominations[i]).rjust(5)}: {qty}')
    else:
        print(f'{str( int(denominations[i]/.01)).rjust(5)}¢: {qty}')
            
    count_denom(dollars % denominations[i], i+1)


if __name__ == "__main__":   
  count_denom(dollars, 0)
