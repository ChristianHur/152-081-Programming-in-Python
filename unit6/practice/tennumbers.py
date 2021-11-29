## Part 1 ###########
#
# Gets 10 unique numbers from user
# @returns a list of 10 unique numbers
#
def getInput():
    tenNumbers = []
    while len(tenNumbers) < 10:
        newNumber = int(input("Enter integer #" + str(len(tenNumbers)+1) + ": "))
        if newNumber in tenNumbers:
            print("\n*** Duplicate number not allowed.  Try again.***")
        else:
            tenNumbers.append(int(newNumber))
        printResult(tenNumbers)
    return tenNumbers


##  PART 2 ############
#
# Removes the minumum number from the 10 numbers
# @returns the list of 9 numbers after the smallest number is removed
#
def removeMin(tenNumbers):
    smallest = tenNumbers[0]    #pick the first number to be the smallest
    for n in tenNumbers:
        if n < smallest:
            smallest = n


    #Pop the smallest number
    tenNumbers.pop( tenNumbers.index(smallest) )
    print("\nThe smallest number removed: ",smallest)

    # The return statement is optional because lists are reference type, 
    # mutating the list in the function also affects the original list 
    # Use return only if you are returning a new list
    # return tenNumbers  

##
# Prints the ten numbers to the console
#
def printResult(tenNumbers):
    print(tenNumbers)

##
# Main entry
#
def main():
    #input - get 10 unique numbers
    print("\nPlease provide 10 unique numbers")
    tenNumbers = getInput()
    
    #output - print the 10 numbers
    print("\nThe 10 unique numbers you entered are:")
    printResult(tenNumbers)
    
    print("\nLet's remove the smallest number")
    input("Press any key to continue...")
    while True and len(tenNumbers) > 0:
        #remove the minimum number
        removeMin(tenNumbers)
        
        #output the 9 numbers
        print("\nThe remaining unique numbers are:")
        printResult(tenNumbers)
        
        more = input("Press enter remove the next smallest number (Q to quit):").upper()
        if more and more[0] == "Q":
            print("\n*** Good-bye.***") 
            break
    else:
        print("\n*** List of number is empty.  Good-bye.***") 
