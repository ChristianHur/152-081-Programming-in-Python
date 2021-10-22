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

Write a program that prompts the user to enter information for vehicles, stocks, or people.  Save the data of each type to their own text file.  Finally, prompt the user to select a file to print.
Ask the user to choose one of the following options for input:
    
    A = Auto
    S = Stocks
    P = Person

For each type, ask the following:

    Auto:    Make, Model, Year, Price
    Stocks:  Company name, Symbol, Stock Price
    Person:  Name, Position, Salary

Keep asking the user until they're done entering data.
'''

# Text files
file_autos = "autos.txt"
file_stocks = "stocks.txt"
file_persons = "persons.txt"

# Error messages
ERROR_INVALID_INPUT = "*** Error:  Invalid input. ***"
ERROR_CANNOT_WRITE_FILE = "*** Error:  Could not write to file. ***"
ERROR_CANNOT_OPEN_FILE = "*** Error:  Could not open file. ***"

# Text messages
TXT_MAKE_SELECTION = "Make A Selection (A=Auto,S=Stock,P=Person,D=Done):"
TXT_PRINT_SELECTION = "Print Selection (A=Auto,S=Stocks,P=Person,Q=Quit):"
TXT_INVALID_SELECTION = "*** Invalid selection.  Try again. ***"
TXT_TRY_AGAIN = "Try again."
TXT_MORE = "More (Y/n)?"
TXT_GREAT = "*** Great! ***"
TXT_GOOD_BYE = "*** Good-bye ***"


def inputAuto():
    """
    Reads input for automobiles and writes to a file
    

    Returns
    -------
    None.

    """
    outfile = openFile(file_autos,"a")    
    if outfile:  
        while True:
            make = input("Enter Make:")
            model = input("Model:")
            year = isValidInput("Year:")
            price = isValidInput("Enter Price:")          
            
            try:
                outfile.write(make + ";" + model + ";" + year + ";" + price + "\n")    
            except:
                print(ERROR_CANNOT_WRITE_FILE)
                return None
            
            if not doMore():
                break   
          
        #Close the text file to seal
        closeFile(outfile)

def inputStock():
    """
    Reads input for stocks and writes to a file

    Returns
    -------
    None.

    """
    outfile = openFile(file_stocks,"a")    
    if outfile:  
        while True:
            company = input("Enter Company Name:")
            symbol = input("Enter Symbol:")
            price = isValidInput("Enter Stock Price:")
            
            try:     
                outfile.write(company + ";" + symbol + ";"+ price + "\n")    
            except:
                print(ERROR_CANNOT_WRITE_FILE)
                return None
            
            if not doMore():
                break   
            
        #Close the text file to seal
        closeFile(outfile)


def inputPerson():
    """
    Reads input for persons and writes to a file

    Returns
    -------
    None.

    """

    outfile = openFile(file_persons,"a")    
    if outfile:    
        while True:
            name = input("Enter Name:")
            position = input("Enter Position:")
            salary = isValidInput("Enter Salary:")  
            
            try:
                # Write record to file
                outfile.write(name + ";" + position + ";" + salary + "\n")    
            except:
                print(ERROR_CANNOT_WRITE_FILE)
                return None
            
            if not doMore():
                break            
        
        #Close the text file to seal
        closeFile(outfile)


def openFile(file, mode):    
    """
    Opens a text file for reading/writing

    Parameters
    ----------
    file : string
        The text file to be open
    mode : string
        The file mode: r,w,a,x

    Returns
    -------
    object
        The file object.

    """
    try:
        f = open(file,mode)
        return f
    except:
        print(ERROR_CANNOT_OPEN_FILE)
    return False

   
def printAuto(file):
    """
    Prints the automobile information

    Parameters
    ----------
    file : string
        The autos text file.

    Returns
    -------
    None.

    """
    infile = openFile(file,"r")
    if infile:    
        lines = infile.readlines()
        for i in range(0,len(lines)):
            items = lines[i].split(";")
            print("Auto #{0}:".format(i+1))
            print("Make:",items[0])
            print("Model:",items[1])
            print("Year:",items[2])
            print("Price: ${:,}".format(int(items[3])))
            print()
        
        #Done - close the text file
        closeFile(infile)


def printStock(file):  
    """
    Prints the stocks information

    Parameters
    ----------
    file : string
        The stocks text file.

    Returns
    -------
    None.

    """
    infile = openFile(file,"r")
    if infile:    
        lines = infile.readlines()
        for i in range(0,len(lines)):
            items = lines[i].split(";")
            print("Stock #{0}:".format(i+1))
            print("Company:",items[0])
            print("Symbol:",items[1])
            print("Price:","${:,.2f}".format(float(items[2])))
            print()
        #Done - close the text file
        closeFile(infile)


def printPerson(file):
    """
    Prints the persons information

    Parameters
    ----------
    file : string
        The persons text file.

    Returns
    -------
    None.

    """
    infile = openFile(file,"r")
    if infile:     
        lines = infile.readlines()
        for i in range(0,len(lines)):
            items = lines[i].split(";")
            print("Person #{0}:".format(i+1))
            print("Name:",items[0])
            print("Position:",items[1])
            print("Salary:","${:,}".format(int(items[2])))
            print()

        #Done - close the text file
        closeFile(infile)


def isValidInput(message):
    """
    Validates numeric input

    Parameters
    ----------
    message : string
        The string message to display to user.

    Raises
    ------
    ValueError
        Non-numeric value.

    Returns
    -------
    val : float
        the numeric input.

    """
    while True:
        try:
            val = input(message)
            if not val.isnumeric():
                raise ValueError(ERROR_INVALID_INPUT)
            return val
        except ValueError as error:
            print(error)
            print(TXT_TRY_AGAIN)


def doMore():
    """
    Prompts user if they want to add more data

    Returns
    -------
    bool
        True (default) if yes, False if NO.

    """
    while True:
        choice = input(TXT_MORE).upper()
        if choice == "N":
            return False
        elif choice == "Y" or choice.strip() == "":
            return True
        else:
            print(ERROR_INVALID_INPUT)

def invalid():
    """
    Prints an invalid selection message

    Returns
    -------
    None.

    """
    print(TXT_INVALID_SELECTION)


def goodBye():
    """
    Prints a good-bye message

    Returns
    -------
    None.

    """
    print("\n" + TXT_GOOD_BYE)

def closeFile(file):
    """
    Closes the specified text file

    Parameters
    ----------
    file : string
        The selected text file.

    Returns
    -------
    None.

    """
    file.close()

def main():
    """
    Main entry to the program

    Returns
    -------
    None.

    """

    # Get input and write to files
    while True:
        choice = input(TXT_MAKE_SELECTION).upper()
        if choice == "D": 
            print("\n" + TXT_GREAT)
            break
    
        if choice == "A":
            inputAuto()
        elif choice =="S":
            inputStock()
        elif choice == "P":
            inputPerson()
        else:
            invalid()

    # Print results
    while True:
        choice = input(TXT_PRINT_SELECTION).upper()
        if choice == "Q": 
            goodBye()
            break
        elif choice == 'A':
            printAuto(file_autos)
        elif choice == 'S':
            printStock(file_stocks)
        elif choice == 'P':
            printPerson(file_persons)
        else:
            invalid()
