# Description

For this exercise, you're going to write a Python program that creates car dearlship that stores an inventory of car and print these cars to the console.

## Part 1:  Implement a class called Vehicle that includes the following:
    
    Fields:

        VIN - string (alphanumeric)
        Make - string
        Model - string
        Year -  int
        Price - int
    
    Method:
        
        default constructor that takes and sets all data fields
        Provide mutators and accessors for all fields
    
## Part 2:  Create a driver program 

Create a Python program that simulates a dealership that owns an inventory of vehicle objects.  Store the vehicles in a dictionary called inventory.  Vehicle data can be obtained using one of the following methods:

**Option 1)**  Prompt the user to enter information for each vehicle, add it to the vehicles dictionary until the user stops (e.g. enter -1 to Quit)

**Option 2)**  Fill the vehicles dictionary with the data from the vehicle.csv file (attached).   Open the file, read and parse each record (line), create a vehicle object with the data, then add it to the vehicles dictionary.  There should be 15 vehicles.

The vehicles are stored in the form:
    
    { VIN1 : vehicle1, VIN2 : vehicle2, VIN3 : vehicle3, etc... }
    
**Sample Run for Opton 1:**
    
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

**Sample Run for Opton 2:**

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
