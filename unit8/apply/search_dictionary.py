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

# Open a text file for reading/writing
def openFile(file, mode):
    try:
        f = open(file,mode)
        return f
    except:
        print('*** Error:  Could not open file. ***')
    return False
