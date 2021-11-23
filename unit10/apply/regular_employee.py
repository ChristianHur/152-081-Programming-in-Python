from employee import Employee

# Subclass
class RegularEmployee(Employee):
    def __init__(self,name,position,department,employeeType,hoursWorked,hourlyRate):
        super().__init__(name, position, department, employeeType, 0)
        self._hoursWorked = hoursWorked
        self._hourlyRate = hourlyRate
        self._regularPay = self.calculateRegularPay()
        self._overTimePay = self.calculateOverTimePay()        
        self.calculatePay()
        
    def calculatePay(self):
        self._weeklyPay = round(self._regularPay + self._overTimePay, 2)
        
    def calculateRegularPay(self):
        if self._hoursWorked >= 40:
            return round(40 * self._hourlyRate, 2)
        return round(self._hoursWorked * self._hourlyRate,2)
    
    def calculateOverTimePay(self):
        if self._hoursWorked > 40:
            return round(self._hourlyRate * (self._hoursWorked - 40) * 1.5, 2)
        return 0

    def getOverTimePay(self):
        return self._overTimePay
    
    def getRegularPay(self):
        return self._regularPay
