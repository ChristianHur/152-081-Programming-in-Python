import urllib.request
import urllib.parse
import json

##
# Prints all books to the console
# @param books - dictionary of books
#
def printBooks(books):
    MAX = 7
    for i in range(len(books)):
        print('-'*MAX)
        print('Book',i+1)
        print('-'*MAX)
        keys = books[i].keys()
        for key in keys:
            print(key.title(),':',books[i][key])
        print()
##
# Main entry to application
#            
def main():
    url = "http://apollo.gtc.edu/~hurc/152-081/unit8/api/"
    webData = urllib.request.urlopen(url)
    results = webData.read().decode()
    webData.close()
    
    #
    ## Convert the json result to a dictionary.
    books = json.loads(results)
    
    printBooks(books)
