## Part 1 ###########
#
# Gets 10 unique numbers from user
# @returns a list of 10 unique numbers
#
def getInput():
    ten_numbers = []
    while len(ten_numbers) < 10:
        new_number = int(input("Enter integer #" + str(len(ten_numbers)+1) + ": "))
        if new_number in ten_numbers:
            print("\n*** Duplicate number not allowed.  Try again.***")
        else:
            ten_numbers.append(int(new_number))
        printResult(ten_numbers)
    return ten_numbers


##  PART 2 ############
#
# Removes the minumum number from the 10 numbers
# @returns the list of ten_numbers reduced by one after the smallest number is removed
#
def removeMin(ten_numbers):
    smallest = ten_numbers[0]    #pick the first number to be the smallest
    for n in ten_numbers:
        if n < smallest:
            smallest = n


    #Pop the smallest number
    ten_numbers.pop( ten_numbers.index(smallest) )
    print("\nThe smallest number removed: ",smallest)

    # The return statement is optional because lists are reference type, 
    # mutating the list in the function also affects the original list 
    # Use return only if you are returning a new list
    # return ten_numbers  

##
# Prints the ten numbers to the console
#
def printResult(ten_numbers):
    print(ten_numbers)

##
# Main entry
#
def main():
    #input - get 10 unique numbers
    print("\nPlease provide 10 unique numbers")
    ten_numbers = getInput()
    
    #output - print the 10 numbers
    print("\nThe 10 unique numbers you entered are:")
    printResult(ten_numbers)
    
    print("\nLet's remove the smallest number")
    input("Press any key to continue...")
    while True and len(ten_numbers) > 0:
        #remove the minimum number
        removeMin(ten_numbers)
        
        #output the 9 numbers
        print("\nThe remaining unique numbers are:")
        printResult(ten_numbers)
        
        more = input("Press enter remove the next smallest number (Q to quit):").upper()
        if more and more[0] == "Q":
            print("\n*** Good-bye.***") 
            break
    else:
        print("\n*** List of number is empty.  Good-bye.***") 
