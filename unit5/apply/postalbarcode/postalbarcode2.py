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
For faster sorting of letters, the United States Postal Service encourages companies that send large volumes of mail to use a bar code denoting the zip code.
The encoding scheme for a five-digit zip code is shown in Figure 13. There are full-height frame bars on each side. The five encoded digits are followed by a check digit, which is computed as follows: Add up all digits and choose the check digit to make the sum a multiple of 10. For example, the zip code 95014 has a sum of 19, so the check digit is 1 to make the sum equal to 20.
Write a program that asks the user for a zip code and prints the bar code. Use : for half bars, | for full bars. For example, 95014 becomes:
    
    ||:|:::|:|:||::::::||:|::|:::|||
'''

##
# Global constants
#
ZIP_CODE = '11000000110010100110010010101001100100011001010100'
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
    start = int(digit)*5  #multiple of 5
    stop  = start+5       #count 5 digits
    return ZIP_CODE[start:stop]

##
# Prints each bar code digit
# @param d  - a zipcode digit
#
def printDigit(d):
    barCode = getCodeDigits(d)
    
    #** Replace a character with another character
    barCode=barCode.replace('1',FULL_BAR)
    barCode=barCode.replace('0',HALF_BAR)   

    #** Or use method chaining **
    #barCode=barCode.replace('1',FULL_BAR).replace('0',HALF_BAR)

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
    print(FULL_BAR,end="")      #Front framebar
    
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

