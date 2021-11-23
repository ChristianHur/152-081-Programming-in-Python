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

from student import Student

def getStudentData():
    print()
    print('*' * 25)
    print('Enter Student Information')
    print('*' * 25)
    
    first = input('First Name: ')
    last = input('Last Name: ')
    year_of_birth = int(input('Birth Year: '))
    major = input('Major: ')
    gpa = float(input('GPA (0-4): '))
    
    return Student(first,last,year_of_birth,major,gpa)

def printResult(students):
    ws = 15  #white space count
    print()
    print('*' * 70)
    print('First'.ljust(ws) + 'Last'.ljust(ws) + 'Year'.ljust(ws) + 'Major'.ljust(ws) + 'GPA')
    print('*' * 70)

    for student in students:
        print(student.getFirst().ljust(ws), end='')
        print(student.getLast().just(ws), end='')
        print(student.getYearOfBirth().just(ws), end='')
        print(student.getMajor().ljust(ws), end='')
        print( '{:.2f}'.format(student.getGpa()) )

def doTask(message):
    while True:
        more = input(message).upper()
        if more not in 'YN':
            print('*** Invalid input.  Try again. ***') 
        else:
            return more == 'N'
    
def main():
    students = []
    done = False
    while not done:
        students.append(getStudentData())
        done = doTask('More (Y/N)? ')
    
    printResult(students)
    
    print("::: Changing Clark Kent's Major to Photography :::")
    students[1].setMajor('Photography')
    
    printResult(students)
    
main()

