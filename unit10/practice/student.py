from person import Person

class Student(Person):
    def __init__(self,first,last,year_of_birth,major,gpa):
        super().__init__(first,last,year_of_birth)
        self._major = major
        self._gpa = gpa
        
    def setMajor(self,major):
        self._major= major
        
    def setGpa(self,gpa):
        self._gpa = gpa
    
    def getMajor(self):
        return self._major
    def getGpa(self):
        return self._gpa
