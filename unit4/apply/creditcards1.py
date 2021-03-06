# -*- coding: utf-8 -*-
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
DESCRIPTION
------------

The last digit of a credit card number is the check digit, which protects
against transcription errors such as an error in a single digit or switching
two digits. The following method is used to verify actual credit card numbers
but, for simplicity, we will describe it for numbers with 8 digits instead of 16:

- Starting from the rightmost digit, form the sum of every other digit.
For example, if the credit card number is 4358 9795, then you form the
sum 5 + 7 + 8 + 3 = 23.

- Double each of the digits that were not included in the preceding step.
Add all digits of the resulting numbers. For example, with the number given
above, doubling the digits, starting with the next-to-last one, yields 18 18 10 8.
Adding all digits in these values yields 1 + 8 + 1 + 8 + 1 + 0 + 8 = 27.

- Add the sums of the two preceding steps. If the last digit of the result is 0,
the number is valid. In our case, 23 + 27 = 50, so the number is valid.

Write a program that implements this algorithm. The user should supply an 8-digit
number, and you should print out whether the number is valid or not.

Here are some sample valid numbers to try:
41235680, 12345674, 98765431, 11224458, 45645645
"""
# card=43589792
temp = input('Enter number:')

sum1 = 0
sum2 = 0

index = len(temp) - 1
while index >= 0:
    '''calculate sum1'''
    sum1 += int(temp[index])
    index -= 2

index = len(temp) - 2
while index >= 0:
    '''caculate sum2'''
    n = int(temp[index]) * 2  # 9+9=18, 4+4=8
    if n >= 10:
        n = str(n)
        sum2 += int(n[0]) + int(n[1])
    else:
        sum2 += n
    index -= 2

# Verify the check digit
total = str(sum1 + sum2)
valid_val = int(total[len(total) - 1])

if valid_val == 0:
    print('Valid')
else:
    print('Invalid')
