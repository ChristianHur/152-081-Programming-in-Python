"""
Unit 4 - Practice (#1) -- using WHILE loop
@author:  Christian Hur

A palindrome is a word that can be read exactly the same forward and backward.
For example, the words "Harrah", "level", "did" are all palindrome, but the
words "Harry", "evil", "dog" are not.   Write a Python program that reads a
word and determine if the word is a palindrome.  Save the file as palindrome.py.

Note:  Use only a for loop or a while loop.  Do not use any built-in shortcuts.
For example, the following shorcuit will automatically reverse a string:

str = "Harry"
new_str = str[::-1]
print (new_str)       # yrraH

"""
#Variables
is_palindrome = True  #force it to be a palindrome

#Input
word = input("Enter a word:")

#Process
lc = 0  #left counter
rc = len(word)-1  #right conter
while lc < rc and is_palindrome:
    if word[lc].lower() != word[rc].lower():
        is_palindrome = False #no match - not a palindrome
    else:
        lc += 1
        rc -= 1

if is_palindrome:
    result = word + " is a palindrome"
else:
    result = word + " is not a palindrome"

#Output
print(result)



