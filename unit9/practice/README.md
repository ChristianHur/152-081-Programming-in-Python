# Description
Implement a class Student. For the purpose of this exercise, a student has a name and a total quiz score. Supply an appropriate constructor and methods getName(), addQuiz(score), getTotalScore(), and getAverageScore().  The constructor should accept the student name and list of scores.  
```python
getName() - returns the student name
addQuiz(score) - adds additional score to the scores list
getTotalScore() - returns the total of the scores list
getAverageScore() - returns the average score
```

## Requirements:
Instantiate a student object
You may create an empty scores list or initialize a default scores list
Prompt the user to enter additional scores, stop entry with a sentinel value (e.g. -1, Q, 0)
Perform the calculations for total score and average score
Print the student name, total score, and average score

## Example:
```python  
student_name = 'Harry Potter'
scores = [90.5, 80, 99, 96.7, 91.25]
student = Student(student_name, scores)
```
The output should print:

```
Name:  Harry Potter
Total Score: 457.45
Average Score: 91.49
```
