
class Student:    
    def __init__(self,name,scores):
        self._name = name
        self._scores = scores
        
    def getName(self):
        return self._name
    
    def setName(self,name):
        self._name = name
        
    def getScores(self):
        return self._scores
        
    def getTotalScore(self):
        return sum(self._scores)
    
    def addScore(self,score):
        self._scores.append(score)
        
    def getAverageScore(self):
        return self.getTotalScore()/len(self._scores)
            
    
