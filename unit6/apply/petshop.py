
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
