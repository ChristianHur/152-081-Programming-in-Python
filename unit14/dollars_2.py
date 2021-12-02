# -*- coding: utf-8 -*-
"""
RECURSION (Recursive function) - a function that calls itself

Write a program that calculates and displays the conversion of an
entered number of dollars into currency denominations:
100s, 50s, 20s, 10s, 5s, 1s, half-dollars, quarters, dimes, nickles, pennies.

Algorithm:  Using slicing operator
"""

dollars = float(input("Enter amount:"))

denominations = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
def count_denom( dollars, denom ):
    
    if len(denom) == 0: return  #DONE
    
    qty = int(dollars // denom[0])
    
    if denom[0] >= 1:
        print(f'${str(denom[0]).rjust(5)}: {qty}')
    else:
        print(f'{str( int(denom[0]/.01)).rjust(5)}¢: {qty}')

    count_denom(dollars % denom[0], denom[1:])


if __name__ == "__main__":   
  count_denom(dollars, denominations)
