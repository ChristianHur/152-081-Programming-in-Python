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
"""

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
