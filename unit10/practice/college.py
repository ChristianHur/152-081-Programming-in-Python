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

