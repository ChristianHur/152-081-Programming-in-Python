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

Write a program that reads the data from a CSV (comma separated value) file
into a list of dictionaries whose keys are first name, last name, email,
company, and salary.

Then the program should prompt the user to enter first name and print the
corresponding values. Stop when the user enters quit.

Pseucode:
    #1 - Build the list of records
        Open the file
        Read each line
        Remove the carriage return
        Break each field into a list
        Create an empty list
        Build a dictionary from this list
        Add this dictonary (record) to the list
    #2 - Read the search term
        While not 999:
            Search the list of records
            If not 999:
                Return the search result found
                Print the result
            else:
                Good-bye
                Exit while
                
Sample run:

Enter search term (999 to exit):DD
--------------------------------------------------
First               Last                Salary
--------------------------------------------------
Freddy              Phillot             $701,920
Thaddus             Kilcoyne            $189,628
Taddeusz            Grigolli            $781,447
Nedda               Aslott              $731,649
Davidde             Winnister           $438,894
Judd                Rooper              $637,802
Nedda               Weekly              $128,444
Paddy               Cleobury            $203,881
Dreddy              Founds              $893,568
Cchaddie            Blazhevich          $232,473
Hedda               Stoltz              $447,558

Enter search term (999 to exit):dy
--------------------------------------------------
First               Last                Salary
--------------------------------------------------
Freddy              Phillot             $701,920
Sandy               Tregaskis           $167,302
Dyane               Cormack             $826,487
Sadye               Elmhirst            $334,576
Lyndy               Petkov              $686,360
Paddy               Cleobury            $203,881
Dreddy              Founds              $893,568

Enter search term (999 to exit):999
*** Good-bye ***                
'''
import sys
import search_dictionary as sd

def main():
    infile = sd.openFile('employees.csv','r')
    if infile:
        records = sd.getRecords(infile)
    else:
        sys.exit(0)
        
    records = sd.getRecords(infile)
    
    while True:
        term = input("Enter search term (999 to exit):").lower()
        if term == '999':
            print("*** Good-bye ***")
            break
        
        result = sd.search(term,records)
        sd.printResult(result)
        
    infile.close()
    
main()
