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

------------
Description:
------------

Write a program that converts a Roman number such as MCMLXXVIII to its decimal number representation.  Use only strings and numeric values.

Symbol	I	V	X	L	C	D	M
Value	1	5	10	50	100	500	1000

Hint: First write a function that yields the numeric value of each of the letters. Then use the following algorithm:

total = 0
string = roman number string
While string is not empty
   If string has length 1, or value(first character of string) is at least value(second character of string)
      Add value(first character of string) to total.
      Remove first character from string.
   Else
      difference = value(second character of string) - value(first character of string)
      Add difference to total.
      Remove first character and second character from string.

Provide the implementations for these functions:

def main()                          # Main entry to start the program
def getRomanNumber()                # Reads, validates, and returns the Roman number
def getValue(val)                   # Retuns the numeric value of a single Roman number (letter)
def printNumericValue(romanNumber)  # Prints the numeric value of a Roman number
'''

#constants
ROMAN_LETTERS = "IVXLCDM"

def getRomanNumber():    
    while True:
        valid = True
        romanNumber = input("Enter a Roman Number:").upper()
        for letter in romanNumber:
            if not letter in ROMAN_LETTERS:
                print("\n*** Invalid input.  Please try again. ***")
                valid = False
                break
        if valid:
            return romanNumber

def getValue(val):
    if val == 'I': return 1
    if val == 'V': return 5
    if val == 'X': return 10
    if val == 'L': return 50
    if val == 'C': return 100
    if val == 'D': return 500
    if val == 'M': return 1000
    
def printNumericValue(romanNumber):
    temp = romanNumber
    total = 0
    while len(temp) > 0:
        if len(temp) == 1 or ( getValue(temp[0]) >= getValue(temp[1])):
            total += getValue(temp[0])
            temp = temp[1:]  # Truncate first value
        else:
            difference = getValue(temp[1]) - getValue(temp[0])
            total += difference
            temp = temp[2:]  # Truncate first two values
    print(f"The numeric value for {romanNumber} is {total}.")

def main():
    romanNumber = getRomanNumber()
    printNumericValue(romanNumber)
    
main()