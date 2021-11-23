from employee import Employee

# Subclass
class Supervisor(Employee):
  def __init__(self,name,position,department,employeeType,salary):
        super().__init__(name, position, department, employeeType, 0)
        self._salary = salary
        
        self.calculatePay()
        
    def calculatePay(self):
        self._weeklyPay = round(self._salary / 52, 2)
