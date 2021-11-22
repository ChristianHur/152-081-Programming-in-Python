## Description

Create two Python modules called  **person.py and student.py**. Implement a superclass **Person** that has a first name, last name, and a year of birth. Implement a subclass called **Student** that extend the **Person** class. A student has a major and GPA. Write the declarations, the constructors, and setter and getter methods for all classes.       
    
Create a main Python program module called  **college.py**. Provide the program that instantiates a Student object and test your program to make sure they work.  
      
### For example:

	student = Student('Clark Kent',1995,'Journalism',4.0)     #Object instantiation and initialization  
	printResult(student)                                      #Prints the student details  
	student.setMajor('Biology')                               #Changes major to Biology  
	printResult(student)                                      #Prints the student details with new a new major
	
### Sample output:  A list of 3 students

	**********************************************************************
	First          Last           Year          Major          GPA
	**********************************************************************
	Lois           Lane           1989           Journalism     3.70
	Clark          Kent           1985           Physics        4.00
	Lex            Luther         1987           Business       3.90
 
### ::: Changing Clark Kent's Major to Photography :::

	Code:  students[1].setMajor('Photography')

	**********************************************************************
	First          Last           Year          Major          GPA
	**********************************************************************
	Lois           Lane           1989           Journalism     3.70
	Clark          Kent           1985           Photography     4.00
	Lex            Luther         1987           Business       3.90
