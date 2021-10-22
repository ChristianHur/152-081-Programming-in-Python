def readInputs():
    """
    Reads inputs into three lists.

    Returns
    -------
    prices : list
        A list of prices.
    isPet : list
        A list of boolean strings.
    nItem : list
        A list of strings.

    """
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
def discount(prices, isPet, nItem):    
    """
    Creates a new discoutned price list for qualified items.

    Parameters
    ----------
    prices : list
        A list of prices.
    isPet : list
        A list of boolean strings.
    nItem : list
        A list of strings.

    Returns
    -------
    list
        Discounted or original list.
    isQualify : boolean
        Whether the item process are qualified for a discount.

    """
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
 
  
def printResult(prices,discountedPrices, isQualify):   
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
        print('Discounted prices:',discountedPrices)
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
    prices, isPet, nItem = readInputs()
    discountedPrices, isQualify = discount(prices,isPet, nItem)
    printResult(prices, discountedPrices, isQualify)
