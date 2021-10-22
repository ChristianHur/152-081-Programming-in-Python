'''
Write a program to simulate a bank transaction. There are two bank accounts: checking and savings. 

First, ask for the initial balances of the bank accounts; reject negative balances and set to zero. 

Then ask for the transaction; options are deposit, withdrawal, and transfer. 

Then ask for the account; options are checking and savings. 

Then ask for the amount; reject transactions that overdraw an account. 

At the end, print the balances of both accounts.
'''

from bank_transaction import main
main()