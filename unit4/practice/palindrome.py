"""
Unit 4 - Practice (#1) -- using FOR loop
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
word_length = len(word)          #get the length of word
mid_point = word_length // 2      #use a midpoint to terminate loop

for index in range( word_length ):
    left_letter  = word[index].lower()
    right_letter = word[-(index+1)].lower()
    if left_letter != right_letter:
        is_palindrome = False #no match - not a palindrome
        break
    elif index >= mid_point:  #if index >= midpoint
        break  #then we're done checking        

if is_palindrome:
    result = word + " is a palindrome"
else:
    result = word + " is not a palindrome"

#Output
print(result)
