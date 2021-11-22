# The Background Information:

You are calculating paycheck amounts for a weekly payroll. There are only 2 types of employees: regular employees and supervisors.
 - Regular employees are paid an hourly wage. They are paid overtime of one-and-one-half (1.5) times their hourly wage for hours worked over 40.
 - Supervisors paycheck amounts are calculated as their yearly salary / 52 (since there are 52 weeks in a year)

## The Program:

Write a program that asks the user to select an employee type (regular or supervisor) and enter the appropriate data for that employee.

 - If the employee is a supervisor, the program should ask for name, position, department, and salary.
- If the employee is a regular, the program should ask for name, position, department, hours worked, and hourly rate

Process and calculate the appropriate weekly pay for the employee.
Print the employee information and their weekly pay. See sample runs at the bottom of this document.

## Part 1: Employee Class (super class)
Create a Python file called employee.py. This is the super class (base class). The super class contains properties that are common to and shared by all subclasses. Include the following in this file.
- Create a class called Employee
- Create a constructor that initializes all the following dependent fields:
	-  Name (string)
	- Position (string)
	- Department (string)
	- Weekly Pay (float, 2 decimal places)
	- Employee type (string) – E or S
- Create Getter and Setter methods to set and return each data field

## Part 2: RegularEmployee Class (subclass)
Create a Python file called regularEmployee.py. A regular employee inherits all the properties in the super class in addition to its own unique properties.
Include the following in this module.
- Create a class called RegularEmployee that extends the Employee super class (make sure you import the Employee class first)
- Constructor that initializes all dependent fields (e.g. fields that are unique only to the RegularEmployee class.)
	- Hours worked (float)
	- Hourly rate (float)
	- Regular pay (float)
	- Overtime pay (float)
- Pass all common fields to the super class
- Create Getter and Setter methods to set and return each data field
- Create a method called calculatePay() to calculate and update the weekly pay in the super class.
- Create a method called calculateOverTimePay() to calculate the overtime pay. This method should update the overtime pay property

## Part 3: Supervisor Class (subclass)
Create a Python file called supervisor.py. A supervisor inherits all the properties in the super class in addition to its own unique properties.
Include the following in this module.
- Create a class called Supervisor that extends the Employee super class (be sure to import the Employee class)
- Constructor that initializes all dependent fields (e.g. fields that are unique to the Supervisor class.)
	- Salary (float)
- Pass all common fields to the super class
- Create Getter and Setter methods to set and return each data field
- Create a method called calculatePay() to calculate and update the weekly pay in the super class.

## Part 4: Driver Application
Create a Python file called work.py. This will be the driver (main) program.
Include the following in this file.
- Import these classes from the appropriate modules: RegularEmployee, Supervisor
- Create a main() method to start the program
- Create function(s) to setup the employee data
- Create function(s) to process and print employee weekly pay to the screen

Use stepwise refinement and break your solution into functions as needed. Once again, use what you've already learned and apply them where they fit.

## Sample Run 1

	Employee or Supervisor [E or S]: S
	Employee name: Christian Hur
	Position: CEO
	Department: IT
	Salary: 150000

	********************** 
	EMPLOYEE WEEKLY PAY
	**********************
	Name: Christian Hur
	Position: CEO
	Department: IT
	Weekly Pay: $2,884.62
	OverTime Pay: $0.00

## Sample Run 2

	Employee or Supervisor [E or S]: E
	Employee name: Lois Lane
	Position: Reporter
	Department: News
	Hours Worked: 50
	Hourly Rate: 100

	***********************
	EMPLOYEE WEEKLY PAY
	***********************
	Name: Lois Lane
	Position: Reporter
	Department: News
	Regular Pay: $4,000.00
	OverTime Pay: $1,500.00
	Weekly Pay: $5,500.00
