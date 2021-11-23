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
Description
------------

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
