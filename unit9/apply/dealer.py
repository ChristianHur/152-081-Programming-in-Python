from vehicle import Vehicle

class Dealership:
    
    def __init__(self):
        self._vehicles = {} #dictionary of vehicles with unique VIN
        
    def getVehicles(self):
        return self._vehicles
    
    def getOneVehicle(self,VIN):
        return self._vehicles[VIN]
    
    def addVehicle(self,vehicle):
        self._vehicles.update({vehicle.getVIN():vehicle})


    