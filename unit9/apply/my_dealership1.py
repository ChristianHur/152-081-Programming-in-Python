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

Create a Python program that simulates a dealership that owns an inventory of vehicle objects.  Store the vehicles in a dictionary called inventory.  Vehicle data can be obtained as follows:
    
Prompt the user to enter information for each vehicle, add it to the vehicles dictionary until the user stops (e.g. enter -1 to Quit).  Use the VIN as the keys for the vehicles.  The vehicles are stored in the form:
    
{ VIN1 : vehicle1, VIN2 : vehicle2, VIN3 : vehicle3, etc... }

    
Sample Run:
    
    Enter Car 1 (VIN, Make, Model, Year, Price):  123FT, Ford, Mustang, 2021, 45000 
    Enter Car 2 (VIN, Make, Model, Year, Price):  345TY, Toyota, Camry, 2022, 35000 
    Enter Car 3 (VIN, Make, Model, Year, Price):  567TS, Tesla, S, 2020, 65000 
    
Output:
    
    ==========================================================================================
    VIN                 MAKE                MODEL               YEAR                PRICE
    ==========================================================================================
    123FT               Ford                Mustang             2021                $45,000
    345TY               Toyota              Camry               2022                $35,000
    567TS               Tesla               S                   2020                $65,000
    ------------------------------------------------------------------------------------------    
    
"""
from vehicle import Vehicle

def getVehicleData(number):
    print()
    print("-"*22)
    print(f"Vehicle {number} Information:")
    print("-"*22)

    record = input("Enter VIN, Make, Model, Year, Price: ")
    record = record.split(',')

    VIN = record[0].strip()
    make = record[1].strip()
    model = record[2].strip()
    year = int(record[3].strip())
    price = int(record[4].strip())
   
    return Vehicle(VIN,make,model,year,price)
    
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

    for VIN, vehicle in inventory.items():
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
    
    number = 1
    more = True
    while more:        
        vehicle = getVehicleData(number)
        inventory.update({vehicle.getVIN() : vehicle})
        number += 1
        more = True if input("More (Y/N)?").upper() == 'Y' else False
        
    printVehicles(inventory)

main()









