"""
Unit 5 - Assignment
@author:  Christian Hur

Create a Python program that asks the user for a 5-digit zip code and prints the bar code.
-------------------------
Background Information
-------------------------
For faster sorting of letters, the United States Postal Service encourages companies that send large volumes of mail to use a bar code denoting the zip code.

The encoding scheme for a five-digit zip code is shown in Figure 13. There are full-height frame bars on each side. The five encoded digits are followed by a check digit, which is computed as follows: Add up all digits and choose the check digit to make the sum a multiple of 10. For example, the zip code 95014 has a sum of 19, so the check digit is 1 to make the sum equal to 20.

Write a program that asks the user for a zip code and prints the bar code. Use : for half bars, | for full bars. For example, 95014 becomes:
    
    ||:|:::|:|:||::::::||:|::|:::|||
"""
##
# Global constants
# 1 = full bar, 0 = half-bar
ZERO     = '11000'
ONE      = '00011'
TWO      = '00101'
THREE    = '00110'
FOUR     = '01001'
FIVE     = '01010'
SIX      = '01100'
SEVEN    = '10001'
EIGHT    = '10010'
NINE     = '10100'
FULL_BAR = '|'
HALF_BAR = ':'

##
# Gets zipcode
# @returns the 5-digit zipcode
def getZipCode():
    return input("Enter a 5-digit zipcode:")

##
# Gets the barcode representation for a digit
# @param digit  - a zipcode digit
# @return the barcode representation
#
def getCodeDigits(digit):
    if digit == '0': return ZERO
    if digit == '1': return ONE
    if digit == '2': return TWO
    if digit == '3': return THREE
    if digit == '4': return FOUR
    if digit == '5': return FIVE
    if digit == '6': return SIX
    if digit == '7': return SEVEN
    if digit == '8': return EIGHT
    if digit == '9': return NINE    

##
# Prints each bar code digit
# @param d  - a zipcode digit
#
def printDigit(d):
    barCode = ""  
    codeDigits = getCodeDigits(d)
    
    for digit in codeDigits:
        if digit == '1':
            barCode += FULL_BAR
        else:
            barCode += HALF_BAR

    print(barCode, end="")

##
# Calculates the check digit
# @param zipCode - the zip code to add
# @return the check digit
def calculateCheckDigit(zipCode):
    sum = 0
    checkDigit = 0
    for digit in zipCode:
        sum += int(digit)    
    if sum % 10 != 0:
        checkDigit = 10 - (sum % 10)
    return str(checkDigit)

##
# Prints the barcode for a zipcode
# @param zipCode  - the zipCode to print
#
def printBarCode(zipCode):
    print(FULL_BAR, end="")      #Front framebar
    
    for d in zipCode:
        printDigit(d)
    
    #Get the check digit and print it's barcode
    checkDigit = calculateCheckDigit(zipCode)
    printDigit(checkDigit)
    
    print(FULL_BAR)      #Back framebar
        
##
# Main entry
#
def main():
    #Input - get 5-digit zipcode
    zipCode = getZipCode()
    
    #Process and Output
    printBarCode(zipCode)

#Program starts here
main()

