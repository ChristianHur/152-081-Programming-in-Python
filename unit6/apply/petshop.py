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
A pet shop wants to give a discount to its clients if they buy one or more pets and at least five other items. The discount is equal to 20 percent of the cost of the other items, but not the pets. Implement a function
def discount(prices, isPet, nItems)

The function receives information about a particular sale. For the ith item, prices[i] is the price before any discount, and isPet[i] is true if the item is a pet.
Write a program that prompts a cashier to enter each price and then a Y for a pet or N for another item. Use a price of –1 as a sentinel. Save the inputs in a list. Call the function that you implemented, and display the discount.
'''

# Read inputs
# Return the lists for prices, isPet, nItem
def readInputs():
    prices = []
    isPet = []
    nItem = []
    while True:
        price = float(input("Enter Price (-1 to quit):"))
        if price == -1:
            break
        if price < 0:
            print("*** INVALID PRICE.  TRY AGAIN. ***")
        else:
            prices.append(price)
            nItem.append(input("Enter item:"))
            while True:
                itemType = input("Is item a pet (Y/N)?").upper()
                if itemType in ['Y','N']:                
                    isPet.append(itemType)
                    break
                print("*** INVALID.  TRY AGAIN. ***")
    return prices, isPet, nItem

# Method to create a discounted prices if qualified
# @param prices - the prices of all items
# @isPet - the list of boolean values for pet and non-pet items
# @nItem - the list of all items
# Return prices or newPrices and isQualify (for discount)
def discount(prices, isPet, nItem):    
    discount = 0.2
    isQualify = False
    newPrices = []
    if "Y" in isPet:
        if isPet.count('N') >= 5:
            isQualify = True
            for i in range(len(prices)):
                if isPet[i] == 'N':
                    newPrices.append(float("{:,.2f}".format(prices[i] - prices[i] * discount)))
                else:
                    newPrices.append(prices[i])
    if len(newPrices) > 0:
        return newPrices, isQualify
    return prices, isQualify
 
# Prints the result to console
# @param prices - the list of item prices
# @param discountedPrices - the new discounted prices
# @param isQualify - boolean (True/False) to check qualification for discount   
def printResult(prices,discountedPrices, isQualify):    
    print("----------------------")
    print('Original prices:',prices)
    if isQualify:
        print('Discounted prices:',discountedPrices)
    else:
        print("Your items do not qualify for a discount.")
    
    print("\n*** Good-bye ***")

# Main entry to program
def main():
    prices, isPet, nItem = readInputs()
    discountedPrices, isQualify = discount(prices,isPet, nItem)
    printResult(prices, discountedPrices, isQualify)
    
main()