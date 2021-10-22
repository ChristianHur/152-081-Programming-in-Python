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
Write a program to simulate a bank transaction. There are two bank accounts: checking and savings. 

First, ask for the initial balances of the bank accounts; reject negative balances and set to zero. 

Then ask for the transaction; options are deposit, withdrawal, and transfer. 

Then ask for the account; options are checking and savings. 

Then ask for the amount; reject transactions that overdraw an account. 

At the end, print the balances of both accounts.
'''

# Main entry to program
def main():
    checking = float(input("Checking Balance:"))
    savings = float(input("Savings Balance:"))
    
    if checking < 0:
        checking = 0
    if savings < 0:
        savings = 0
        
    transaction = input("Transaction [D=Deposit, W=Withdrawal, T=Transfer]:").upper()
    account = input("Select Account [C=Checking, S=Savings]:").upper()
    amount = float(input("Enter Amount:"))
    
    if transaction == 'D':
        if amount < 0:
            amount = 0
        
        if account == 'C':
            checking += amount
            print("\n>>> ${:,.2f} was deposited into Checking.".format(amount))
        else:
            savings += amount
            print("\n>>> ${:,.2f} was deposited into Savings.".format(amount))
    
    elif transaction == 'W':
        if account == 'C':
            if amount <= checking:
                checking -= amount
                print("\n>>> ${:,.2f} was withdrawn from Checking.".format(amount))
            else:
                print("\n>>> *** Insufficient funds. ***")
        else:
            if amount <= savings:
                savings -= amount
                print("\n>>> ${:,.2f} was withdrawn from Savings.".format(amount))
            else:
                print("\n>>> *** Insufficient funds. ***")
    
    else:
        if account == 'C':
            if amount <= checking:
                savings += amount
                checking -= amount
                print("\n>>> ${:,.2f} was transferred to Savings.".format(amount))
            else:
                print("\n>>> *** Insufficient funds. ***")
        else:
            if amount <= savings:
                checking += amount
                savings -= amount
                print("\n>>> ${:,.2f} was transferred to Checking.".format(amount))
            else:
                print("\n>>> *** Insufficient funds. ***")
    
    checking = "${:,.2f}".format(checking)
    savings = "${:,.2f}".format(savings)
    
    print()
    print("*" * 15, "BALANCE", "*" * 16)
    print(f'\tChecking:\t{checking:>20}')
    print(f"\tSavings:\t{savings:>20}")
    print("*" * 40)

main()