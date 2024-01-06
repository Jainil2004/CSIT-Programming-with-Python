# Question 1

"""
1. Two of Python’s built-in functions are min and max. In the Python shell, execute the following function calls:
a. min(2, 3, 4)
b. max(2, -3, 4, 7, -5)
c. max(2, -3, min(4, 7), -5)
"""

# Answers
"""
a. 2
b. 7
c. Now here the inner part evaluates to 4, and the maximum would evaluate to 4
"""

# Question 2

"""
2. For the following function calls, in what order are the subexpressions evaluated?
a. min(max(3, 4), abs(-5))
b. abs(min(4, 6, max(2, 8)))
c. round(max(5.572, 3.258), abs(-2))
"""

# Answers
"""
a. max(3, 4) evaluates to 4 and abs(-5) evaluates to 5, so min would be 4 
b. Inner part max(2, 8) evaluates to 8, middle part min(4, 6, 8) evaluates to 4, outer part abs(4) evaluates to 4
c. Inner part max(5.572, 3.258) evaluates to 5.572, outer part round(5.572, abs(-2)) evaluates to 5.57 (rounded to 2 decimal places)
"""

# Question 3

"""
3. Following the function design recipe, define a function that has one parameter, a number, and returns that number tripled.
"""

# Answer
def triple(num):
    return num * 3


# Question 4

"""
4. Following the function design recipe, define a function that has two parameters, both of which are numbers, and returns the absolute value of the difference of the two. Hint: Call built-in function abs.
"""

# Answer
def absDifference(num1, num2):
    return abs(num1 - num2)


# Question 5

"""
5. Following the function design recipe, define a function that has one parameter, a distance in kilometers, and returns the distance in miles. (There are 1.6 kilometers per mile.)
"""

# Answer
def kmConverter(km):
    return km / 1.6


# Question 6

"""
6. Following the function design recipe, define a function that has three parameters, grades between 0 and 100 inclusive, and returns the average of those grades.
"""

# Answer
def avgGrade(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3


# Question 7

"""
7. Following the function design recipe, define a function that has four parameters, all of them grades between 0 and 100 inclusive, and returns the average of the best 3 of those grades. Hint: Call the function that you defined in the previous exercise.
"""

# Answer
def topOfThreeGrade(grade1, grade2, grade3, grade4):
    all_grades = [grade1, grade2, grade3, grade4]
    return (sum(all_grades) - min(all_grades)) / 3.0


# Question 8

"""
8. Complete the examples in the docstring and then write the body of the following function:

def weeks_elapsed(day1, day2): 
""" (int, int) -> int 
"""
     day1 and day2 are days in the same year. Return the number of full weeks
     that have elapsed between the two days.
     >>> weeks_elapsed(3, 20)
     2
     >>> weeks_elapsed(20, 3)
     2
     >>> weeks_elapsed(8, 5)
     >>> weeks_elapsed(40, 61)
"""

# Answer

def weeks_elapsed(day1, day2):
    return int(abs(day1 - day2) / 7)


# Question 9

# Answer

"""
Description        Example
Parameter           num 
Argument            3   
Function name       square
Function call       square(3)
"""

# Question 10

"""
10. Given the following function definition:

def square(num):
    return num**2

Complete the examples in the docstring and then write the body of the function.

Examples:
    >>> square(3)
    9
    >>> square(-5)
    25
    >>> square(0)
    0
    >>> square(2.5)
    6.25
"""

# Answer

def square(num):
    return num**2
