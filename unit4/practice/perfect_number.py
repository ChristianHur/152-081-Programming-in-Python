"""
Unit 4 - Assignment (#1)
@author:  Christian Hur

Write an application that displays every perfect number from 1 through 1,000.
A perfect number is one that equals the sum of all the numbers that divide
evenly into it. For example, 6 is perfect because 1, 2, and 3 divide evenly
into it, and their sum is 6; however, 12 is not a perfect number
because 1, 2, 3, 4, and 6 divide evenly into it, and their sum is greater than 12.
"""

#Variables
number = 1000   #input

#Process
for n in range(1,number+1):     #to include 1000
    sum = 0                     #accumulator
    for m in range(1,n):        #from 1 up to n (exclude n)
        if n % m == 0:
            sum += m            #store the divisor
    
    if sum == n:
        #Output
        print(n)                #print magic number
        
