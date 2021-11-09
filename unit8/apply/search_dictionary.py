import sys

# Read all records from file
# Return the list of records
def getRecords(infile):
    # TO-DO
    pass

# Search the records with the term
# Return the list of records matching term
def search(term,records):
    # TO-DO
    pass

# Print the search result
def printResult(result):
    # TO-DO
    pass

def main():
    try:
        infile = open("employeess.csv")
    except:
        print('*** ERROR:  Could not open file ***')
        sys.exit(0)
        
    records = getRecords(infile)
    
    while True:
        term = input("Enter search term (999 to exit):").lower()
        if term == '999':
            print("*** Good-bye ***")
            break
        
        result = search(term,records)
        printResult(result)
  
    infile.close()
