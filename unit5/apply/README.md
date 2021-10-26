## Description

Write a program that converts a Roman number such as MCMLXXVIII to its decimal number representation.  Use only strings and numeric values.

      Symbol:	I	V	X	L	C	D	M
      Value:	1	5	10	50	100	500	1000

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

    def main()                        # Main entry to start the program
    def getRomanNumber()              # Reads, validates, and returns the Roman number
    def getValue(val)                 # Retuns the numeric value of a single Roman number (letter)
    def printNumericValue(romanNumber)  # Prints the numeric value of a Roman number
