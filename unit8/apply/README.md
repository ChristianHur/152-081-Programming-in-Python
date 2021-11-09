# Description

Write a program that reads the data from a CSV (comma separated value) file into a list of dictionaries whose keys are first name, last name, email, company, and salary.

Then the program should prompt the user to enter first name and print the corresponding values. Stop when the user enters quit.

## Pseucode:
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
                
## Sample run:

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
