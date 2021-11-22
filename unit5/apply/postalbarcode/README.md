# Description

Create a Python program that asks the user for a 5-digit zip code and prints the bar code.

## Background Information
For faster sorting of letters, the United States Postal Service encourages companies that send large volumes of mail to use a bar code denoting the zip code.

![](https://github.com/ChristianHur/152-081-Programming-in-Python/blob/main/unit5/apply/postalbarcode/images/figure1.png)

The encoding scheme for a five-digit zip code is shown in Figure 2. There are full-height frame bars on each side. The five encoded digits are followed by a check digit, which is computed as follows: Add up all digits and choose the check digit to make the sum a multiple of 10. For example, the zip code `95014` has a sum of `19`, so the check digit is `1` to make the sum equal to `20`.

![](https://github.com/ChristianHur/152-081-Programming-in-Python/blob/main/unit5/apply/postalbarcode/images/figure2.png)

Each digit of the zip code, and the check digit, is encoded according to the table below, where
0 denotes a half bar and 1 a full bar:

![](https://github.com/ChristianHur/152-081-Programming-in-Python/blob/main/unit5/apply/postalbarcode/images/figure3.png)

The digit can be computed easily from the bar code using the column weights 7, 4, 2, 1, 0. For
example, 01100 is 0 × 7 + 1 × 4 + 1 × 2 + 0 × 1 + 0 × 0 = 6. The only exception is 0, which
would yield 11 according to the weight formula.

Use `:` for half bars, `|` for full bars. 

For example, 95014 becomes:
    
    ||:|:::|:|:||::::::||:|::|:::|||
    
Provide and implement these functions:

        def main()                  # Main entry to start the program
        def getDigit()              # Reads and return the 5-digit zip code
        def printDigit(d)           # Prints the bar code for a digit
        def printBarCode(zipCode)   # Prints the encoded bar code

