# Super class
class Employee:
    def __init__(self,name,position,department,employeeType,weeklyPay):
        self._name = name
        self._position = position
        self._department = department
        self._weeklyPay = weeklyPay
        self._type = employeeType
        
    def setName(self,name): self._name = name
    def setPosition(self,position): self._position = position
    def setDepartment(self,department): self._department = department
    def setWeeklyPay(self,weeklyPlay): self._weeklyPay = weeklyPlay
        
    def getName(self): return self._name
    def getPosition(self): return self._position
    def getDepartment(self): return self._department
    def getWeeklyPay(self): return self._weeklyPay
    def getType(self): return self._type
    
    def __repr__(self):
       return str([self._name,self._position,self._department])
      
