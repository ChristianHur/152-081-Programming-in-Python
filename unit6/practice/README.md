# Description

Write a program that reads 10 unique numbers and removes the smallest number from thet list.
adds them to a list if they aren’t 
### Part 1
Write a function *getInput()* to read 10 unique numbers. When the list contains ten numbers, 
the program displays the contents.

### Part 2
Write a function *removeMin()* that removes the minimum value from a list 
without using the `min` function or `remove` method.

### Part 3
Prompts the user to keep removing the next smallest from the list until they
enter a sentinel value ('Q') to quit the program.

### Sample Run
```
Please provide 10 unique numbers

Enter integer #1: 2
[2]

Enter integer #2: 4
[2, 4]

Enter integer #3: 3
[2, 4, 3]

Enter integer #4: 3

*** Duplicate number not allowed.  Try again.***
[2, 4, 3]

Enter integer #4: 6
[2, 4, 3, 6]

Enter integer #5: 8
[2, 4, 3, 6, 8]

Enter integer #6: 89
[2, 4, 3, 6, 8, 89]

Enter integer #7: 32
[2, 4, 3, 6, 8, 89, 32]

Enter integer #8: 12
[2, 4, 3, 6, 8, 89, 32, 12]

Enter integer #9: 10
[2, 4, 3, 6, 8, 89, 32, 12, 10]

Enter integer #10: 9
[2, 4, 3, 6, 8, 89, 32, 12, 10, 9]

The 10 unique numbers you entered are:
[2, 4, 3, 6, 8, 89, 32, 12, 10, 9]

Let's remove the smallest number

Press any key to continue...

The smallest number removed:  2

The remaining unique numbers are:
[4, 3, 6, 8, 89, 32, 12, 10, 9]

Press enter remove the next smallest number (Q to quit):

The smallest number removed:  3

The remaining unique numbers are:
[4, 6, 8, 89, 32, 12, 10, 9]

Press enter remove the next smallest number (Q to quit):

The smallest number removed:  4

The remaining unique numbers are:
[6, 8, 89, 32, 12, 10, 9]

Press enter remove the next smallest number (Q to quit):

The smallest number removed:  6

The remaining unique numbers are:
[8, 89, 32, 12, 10, 9]

Press enter remove the next smallest number (Q to quit):Q

*** Good-bye.***
```
