## Description

Write a program that converts a Roman number such as MCMLXXVIII to its decimal number representation.  Use only strings and numeric values.

|Symbol |I|V|X|L|C|D|M|
-|-|-|-|-|-|-|-|
**Value**|1|5|10|50|100|500|1000


Numbers are formed according to the following rules.

 a.  Only numbers up to 3,999 are represented. 
 
 b.  As in the decimal system, the thousands, hundreds, tens, and ones are expressed separately.
 
 c.  The numbers 1 to 9 are expressed as:
 
| Symbol |I|II|III|IV|V|VI|VII|VIII|IX|
|-|-|-|-|-|-|-|-|-|-|
|**Value**|1|2|3|4|5|6|7|8|9|


As you can see, an `I` preceding a `V` or `X` is subtracted from the value, and you can never have more than three `I`'s in a row.

d. Tens and hundreds are done the same way, except that the letters X, L, C and C, D, M are used instead of I, V, X, respectively.

Your program should take an input, such as 1978, and convert it to Roman numerals, MCMLXXVIII.

## Algorithm
First write a function that yields the numeric value of each of the letters. Then use the following algorithm:

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
