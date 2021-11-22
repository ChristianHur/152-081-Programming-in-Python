'''
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
-------------------------
Description
-------------------------
Write a program that calculates and displays the conversion of an entered number of dollars into currency denominations—100s, 50s, 20s, 10s, 5s, and 1s. 
'''

# Input
dollars = int(input("Enter an amount:"))

# Process
hundreds = dollars // 100
dollars %= 100
fifties = dollars // 50
dollars %= 50
twenties = dollars // 20
dollars %= 20
tens = dollars // 10
dollars %= 10
fives = dollars // 5
ones = dollars % 5

# Output
print("$100 bills:", hundreds)
print("$ 50 bills:", fifties)
print("$ 20 bills:", twenties)
print("$ 10 bills:", tens)
print("$  5 bills:", fives)
print("$  1 bills:", ones)
