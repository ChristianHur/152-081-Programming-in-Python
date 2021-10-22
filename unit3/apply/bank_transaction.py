
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
