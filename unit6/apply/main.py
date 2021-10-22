"""
A pet shop wants to give a discount to its clients if they buy one or more pets and at least five other items. The discount is equal to 20 percent of the cost of the other items, but not the pets. Implement a function
def discount(prices, isPet, nItems)

The function receives information about a particular sale. For the ith item, prices[i] is the price before any discount, and isPet[i] is true if the item is a pet.
Write a program that prompts a cashier to enter each price and then a Y for a pet or N for another item. Use a price of –1 as a sentinel. Save the inputs in a list. Call the function that you implemented, and display the discount.
"""
from petshop import main
main()