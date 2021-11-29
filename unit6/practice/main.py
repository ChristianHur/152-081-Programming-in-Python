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
A pet shop wants to give a discount to its clients if they buy one or more
pets and at least five other items. The discount is equal to 20 percent of
the cost of the other items, but not the pets. Implement a function
def discount(prices, isPet, nItems)

The function receives information about a particular sale. For the ith item,
prices[i] is the price before any discount, and isPet[i] is true if the item
is a pet.

Write a program that prompts a cashier to enter each price and then a Y for a
pet or N for another item. Use a price of –1 as a sentinel. Save the inputs
in a list. Call the function that you implemented, and display the discount.
'''
import tennumbers as tn
tn.main()
