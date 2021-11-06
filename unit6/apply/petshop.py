def readInputs():
    """
    Reads inputs into three lists.

    Returns
    -------
    prices : list
        A list of prices.
    isPet : list
        A list of boolean values.
    nItems : list
        A list of strings.

    """
    prices = []
    isPet = []
    nItems = []
    while True:
        price = float(input("Enter Price (-1 to quit):"))
        if price == -1:
            break
        if price < 0:
            print("*** INVALID PRICE.  TRY AGAIN. ***")
        else:
            prices.append(price)
            nItems.append(input("Enter item:"))
            while True:
                itemType = input("Is item a pet (Y/N)?").upper()
                if itemType in ['Y','N']:
                    if itemType == 'Y':
                        isPet.append(True)
                    else:
                        isPet.append(False)
                    break
                print("*** INVALID INPUT.  TRY AGAIN. ***")
    return prices, isPet, nItems

# Method to create a discounted prices if qualified
def discount(prices, isPet, nItems):    
    """
    Creates a new discounted price list for qualified items.

    Parameters
    ----------
    prices : list
        A list of prices.
    isPet : list
        A list of boolean values.
    nItems : list
        A list of strings.

    Returns
    -------
    list
        Discounted or original list.
    isQualify : boolean
        Whether the item prices are qualified for a discount.

    """
    discount = 0.2
    isQualify = False
    newPrices = []
    if True in isPet:
        if isPet.count(False) >= 5:
            isQualify = True
            for i in range(len(nItems)):
                if isPet[i] == False:
                    newPrices.append(float("{:,.2f}".format(prices[i] - prices[i] * discount)))
                else:
                    newPrices.append(prices[i])
    if len(newPrices) > 0:
        return newPrices, isQualify
    return prices, isQualify
 
  
def printResult(prices, discountedPrices, isQualify):   
    """
    Prints the results to the console

    Parameters
    ----------
    prices : list
        The original prices list.
    discountedPrices : list
        The discounted prices list.
    isQualify : boolean
        Flag to print discounted prices list.

    Returns
    -------
    None.

    """
    print("----------------------")
    print('Original prices:',prices)
    if isQualify:
        print('Discounted prices:', discountedPrices)
    else:
        print("Your items do not qualify for a discount.")
    
    print("\n*** Good-bye ***")


def main():
    """
    Main entry to the program

    Returns
    -------
    None.

    """
    prices, isPet, nItems = readInputs()
    discountedPrices, isQualify = discount(prices, isPet, nItems)
    printResult(prices, discountedPrices, isQualify)
