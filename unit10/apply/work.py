from regular_employee import RegularEmployee
from supervisor import Supervisor

def getEmployeeData(employeeType):
  #TODO
  pass

def printWeeklyPay(employee):
  #TODO
  pass

def doMore():
    while True:
        more = input('More (Y/N):').upper()
        if more not in 'YN':
            print('*** Invalid input.  Try again. ***') 
        else:
            return more == 'N'   

def main():
  #TODO
  pass

main()
