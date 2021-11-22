
class Vehicle:
    def __init__(self,VIN,make,model,year,price):
        self._VIN = VIN
        self._make = make
        self._model = model
        self._year = year
        self._price = price
        
    def setVIN(self,VIN):
        self._VIN = VIN
    
    def setMake(self,make):
        self._make = make
        
    def setModel(self,model):
        self._model = model
        
    def setYear(self,year):
        self._year = year
        
    def setPrice(self,price):
        self._price = price
    
    def getVIN(self):
        return self._VIN
    
    def getMake(self):
        return self._make
    
    def getModel(self):
        return self._model
    
    def getYear(self):
        return self._year
    
    def getPrice(self):
        return self._price
    
