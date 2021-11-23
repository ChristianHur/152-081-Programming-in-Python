"""
Unit 4 - Practice (#2)
@author:  Christian Hur

Write a Python program that reads an integer value from the console and converts
it into its binary equivalent . For example, if the user provides the input 13,
the output should be:  1101. 
"""

#Variable
binary = ""

#Input
number = int(input("Enter a positive integer:"))
temp = number  #preserve original number for printing

#Process
while temp != 0:
    binary = str(temp % 2) + binary
    temp = temp // 2

#Output
print("The binary of {} is {}".format(number,binary))
