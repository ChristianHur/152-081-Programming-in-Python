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

------------
Description:
------------

Implement a class Student. For the purpose of this exercise, a student has
a name and a total quiz score. Supply an appropriate constructor and methods
getName(), addQuiz(score), getTotalScore(), and getAverageScore().
The constructor should accept the student name and list of scores.  

getName() - returns the student name
addQuiz(score) - adds additional score to the scores list
getTotalScore() - returns the total of the scores list
getAverageScore() - returns the average score

Requirements:
    Instantiate a student object
    You may create an empty scores list or initialize a default scores list
    Prompt the user to enter additional scores, stop entry with a
    sentinel value (e.g. -1, Q, 0)
    Perform the calculations for total score and average score
    Print the student name, total score, and average score

Example:
    
    student name:  Christian Hur
    scores = [90.5,80,99,96.7,91.25]
    
    The output should print:
        
        Name:  Christian Hur
        Total Score: 457.45
        Average Score: 91.49
"""

import random
from student import Student

def getScores(student):
    while True:
        try:
            score = input("Enter score (-1 to Stop): ")
            if score == '-1':
                break
            student.addScore(float(score))           
        except:
            print('*** Invalid input.  Try again. ***')

def printScores(student):
    print("="*55)
    print("Name".ljust(20) + "Total Score".ljust(20) + "Avg Score")
    print("="*55)
    print(student.getName().ljust(20) +
          str(round(float(student.getTotalScore()),2)).ljust(20) +
          str(round(float(student.getAverageScore()),2)))
    
def main():
    scores=[]
    for i in range(10):
        n = round(random.uniform(70,100),2)
        scores.append(n)
        print(n)
    student = Student('Christian',scores)
    
    getScores(student)
    printScores(student)        
    

main()
