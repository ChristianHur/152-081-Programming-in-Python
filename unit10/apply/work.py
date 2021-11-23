from regular_employee import RegularEmployee
from supervisor import Supervisor

def getEmployeeData(employeeType):
    name = input('Employee name: ')
    position = input('Position: ')
    department = input('Department: ')
    if employeeType == 'E':
        hoursWorked = float(input('Hours Worked: '))
        hourlyRate = float(input('Hourly Rate: '))
        employee = RegularEmployee(name, position, department, employeeType, hoursWorked,hourlyRate)
    else:
        salary = float(input('Salary: '))
        employee = Supervisor(name, position, department, employeeType, salary)
    return employee

def printWeeklyPay(employee):
    
    # Format currency to two decimal places
    if employee.getType() == 'E':
        overTimePay = '{:,.2f}'.format(employee.getOverTimePay())
        regularPay = '{:,.2f}'.format(employee.getRegularPay())
    else:
        overTimePay = '{:,.2f}'.format(0)
        regularPay = '{:,.2f}'.format(0)
        
    weeklyPay = '{:,.2f}'.format(employee.getWeeklyPay())
    
    # Print to screen
    print()
    print('*'*20)
    print('EMPLOYEE WEEKLY PAY')
    print('*'*20)
    print(f'Name: {employee.getName()}')
    print(f'Position: {employee.getPosition()}')
    print(f'Department: {employee.getDepartment()}')
    if employee.getType() == 'E':
        print(f'Regular Pay: ${regularPay}')
    print(f'Weekly Pay: ${weeklyPay}')
    print(f'OverTime Pay: ${overTimePay}')

def doMore():
    while True:
        more = input('More (Y/N):').upper()
        if more not in 'YN':
            print('*** Invalid input.  Try again. ***') 
        else:
            return more == 'N'            
                
def main():
    
    done = False
    while not done:
        employee = None
        while True:
            employeeType = input('Employee or Supervisor [E or S]: ').upper()
            if employeeType in 'ES':                
                employee = getEmployeeData(employeeType)
                break
            else:
                print('*** Invalid input.  Try again. ***')
    
        printWeeklyPay(employee)
        done = doMore()    
    
main()
