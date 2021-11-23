class Person:
  
    def __init__(self,first,last,year_of_birth):
        self._first = first
        self._last = last
        self._year_of_birth = year_of_birth
        
    def setFirst(self,first):
        self._first = first
        
    def setLast(self,last):
        self._last = last
        
    def setYearOfBirth(self,year_of_birth):
        self._year_of_birth = year_of_birth
        
    def getFirst(self):
        return self._first
      
    def getLast(self):
        return self._last
      
    def getYearOfBirth(self):
        return self._year_of_birth
      
