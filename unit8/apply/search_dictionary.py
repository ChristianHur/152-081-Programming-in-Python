# Read all records from file
# Return the list of records
def getRecords(infile):
    records = []
    for line in infile:
        line = line.strip('\n')
        line = line.split(',')
        data = {}
        data['first'] = line[0]
        data['last']=line[1]
        data['email']=line[2]
        data['company']=line[3]
        data['salary']=line[4]
        records.append(data)
    return records

# Search the records with the term
# Return the list of records matching term
def search(term,records):
    result = []    
    for record in records:
        if term in record['first'].lower():
            result.append(record)
    return result

# Print the search result
def printResult(result):
    spaces = 20    
    
    # Print heading
    print('-' * 50)
    print("First".ljust(spaces) + "Last" .ljust(spaces) + "Salary")
    print('-' * 50)
    
    # Print records
    for record in result:
        spaces = 20
        print(record['first'].ljust(spaces), end="")
        print(record['last'].ljust(spaces), end="")
        print("$" + "{:,}".format(int(record['salary'])))

# Open a text file for reading/writing
def openFile(file, mode):
    try:
        f = open(file,mode)
        return f
    except:
        print('*** Error:  Could not open file. ***')
    return False
