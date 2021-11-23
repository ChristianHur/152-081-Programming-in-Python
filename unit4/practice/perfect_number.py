"""
MIT License

Copyright (c) 2021 Christian Hur (Gateway Technical College)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

------------
Description
------------

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
        
