"""
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

For this exercise, you're going to write a Python program that creates car dearlship that stores an inventory of car and print these cars to the console.

Part 1:  Implement a class called Vehicle that includes the following:
    
    Fields:

        VIN - string (alphanumeric)
        make - string
        model - string
        year -  int
        price - int
    
    Method:
        
        default constructor that takes and sets all data fields
        Provide mutators and accessors for all fields    

Part 2:  Create a driver program 

Create a Python program that simulates a dealership that owns an inventory of vehicle objects.  Store the vehicles in a dictionary called inventory.  Vehicle data can be obtained from a CSV file.
    
Fill the inventory dictionary with the data from the vehicle.csv file (attached).   Open the file, read and parse each record (line), create a vehicle object with the data, then add it to the inventory dictionary.   Use the VIN as the keys for the vehicles.  There should be 15 vehicles stored in the form:
    
{ VIN1 : vehicle1, VIN2 : vehicle2, VIN3 : vehicle3, etc... }
    
Sample Run:

Output:
    
    ==========================================================================================
    VIN                 MAKE                MODEL               YEAR                PRICE
    ------------------------------------------------------------------------------------------
    WP0AA2A92CS661189   GMC                 Envoy XL            2002                $55,712
    2G4GT5GX6E9095341   Pontiac             Vibe                2009                $45,333
    1G6YV34A945245092   Ferrari             599 GTB Fiorano     2008                $73,892
    WAUBH74F66N258296   Ford                EXP                 1988                $84,393
    WBABD53425P639601   Chrysler            Town & Country      2007                $89,646
    5UXFE43568L586092   Mitsubishi          Endeavor            2004                $94,956
    1G6DM5EY3B0367966   Volkswagen          Jetta               1984                $83,202
    2C4RDGEG5ER151231   Dodge               Charger             2007                $17,172
    WBAUC9C58DV549228   Pontiac             Firebird            1984                $58,594
    1FTEW1CM6CK082847   Buick               Regal               1995                $69,014
    2C4RDGBG7FR808214   Mazda               Mazda2              2012                $13,516
    1G4GD5ER1CF519207   Suzuki              Swift               1993                $68,144
    1D4PT2GK5AW564141   Ford                Excursion           2004                $43,187
    5GAKRBED0CJ344580   Lamborghini         Gallardo            2010                $34,509
    2G4WC552871264621   Buick               Century             1987                $46,854
    ------------------------------------------------------------------------------------------
    
"""
import sys
from vehicle import Vehicle

def getVehicleData(inventory):
    
    try:
        inFile = open('vehicles.csv','r')
    except:
        print("*** ERROR:  Couldn't open file. ***")
        sys.exit(0)
    
    for record in inFile.readlines():
        record = record.strip('\n')
        record = record.split(',')
        
        VIN = record[0].strip()
        make = record[1].strip()
        model = record[2].strip()
        year = int(record[3].strip())
        price = int(record[4].strip())  
        
        # Add a vehicle to the inventory
        inventory.update({VIN: Vehicle(VIN,make,model,year,price)})
    
def printVehicles(inventory):
    tab = 20
    dash_count = 90
    
    print()
    print("=" * dash_count)
    
    # print("VIN" + " " * (tab - 3) + 
    #       "MAKE" + " " * (tab - 4) + 
    #       "MODEL" + " " * (tab - 5) + 
    #       "YEAR" + " " * (tab - 4) + 
    #       "PRICE")

    print('VIN'.ljust(tab) +
          'MAKE'.ljust(tab) +
          'MODEL'.ljust(tab) +
          'YEAR'.ljust(tab-10) +
          'PRICE')
    
    print("-" * dash_count)

    for VIN,vehicle in inventory.items():
        make = vehicle.getMake()
        model = vehicle.getModel()
        year = vehicle.getYear()
        price = "${:,}".format(vehicle.getPrice())
        
        # print(VIN + " " * (tab - len(VIN)),end="")
        # print(make + " " * (tab - len(make)),end="")
        # print(model + " " * (tab - len(model)),end="")
        # print(str(year) + " " * (tab - 4),end="")
        # print( price )

        print(VIN.ljust(tab) +
              make.ljust(tab) +
              model.ljust(tab) +
              str(year).ljust(tab-10) +
              str(price))

    print("-" * dash_count)
        
def main():    
    inventory = {}
    getVehicleData(inventory)
    printVehicles(inventory)


main()









