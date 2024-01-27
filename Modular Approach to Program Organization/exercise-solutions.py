# exercise-solutions of the chapter A Modular Approach to Program Organization

# problem 1
print("problem 1")
# Import module math, and use its functions to complete the following exercises
# a. write an expression that produces the floor of -2.8
import math
num1 = -2.8
floor_number = math.floor(num1)
print(f"1.a. {floor_number}")
# solution: the math.floor() function returns the largest integer less than or equal to the given number 
#           in this case it is -2.8. and hence the largest integer that is less than -2.8 is -3.
 
# b. write an expression that rounds the value of -4.3 and then produces 
# the absolute value of that result.
num2 = -4.3
rounded_number = round(-4.3)
absolute_value = abs(rounded_number)
print(f"1.b. {absolute_value}")
# solution: the round function first rounds the number to the nearest integer in this case it is -4
#           and finally then the abs function provides the absolute value which is 4.

# c. write an expression that produces the ceiling of the sine of 34.5
angle_in_degrees = 34.5
angle_in_radians = math.radians(angle_in_degrees)
sine_val = math.sin(angle_in_radians)
ceil_val = math.ceil(sine_val)
print(f"1.c. {sine_val}")
# solution: to find the ceil of the angle we first have to convert the angle into radians 
#           as the math.sin function takes in the angle in radians. after that we can feed 
#           the sine value into the math.ceil functions which would give us the ceiling
#           value of the sine.

# problem 2
print("\nproblem2\n")
# in the following exercises, you will work with python's calendar module:
# a. visit the python documentation website at http://docs.python.org/release/3.6.0/py-modindex.html
# and look at the documentation on module calendar
# solution: please visit the site at http://docs.python.org/release/3.6.0/py-modindex.html for documentation

# b. import module calendar
import calendar 
# solution: this imports the calendar module in our program.

# c. using function help, read the description of function isleap
print("2.c. ")
help(calendar.isleap)
# solution: this code will print the what the functions does.

# d. use isleap to determine the next year
next_year = 2025
print(f"2.d. is the next year leap? :{calendar.isleap(next_year)}")
# solution: since year 2025 is not a leap year the function returns false.

# e. use dir to get a list of what calendar contains
func_of_dir = (dir(calendar))
print("2.e. list of all the functions calendar module is capable of")
for func in func_of_dir:
    print(func)
# solution: the dir function returns the list of all the different functions offered by 
#           the module calendar.

# f. find and use a function in module calendar to determine how many leap years
# there will be between the years 2000 and 2050, inclusive
def leap_years(start, end):
    leap_years_count = 0
    for year in range(start, end+1):
        if calendar.isleap(year):
            leap_years_count += 1
    return leap_years_count
start_year = 2000
end_year = 2050
print(f"\n2.g. leap years in the range of {start_year} and {end_year} = {leap_years(start_year, end_year)}")
# solution: the calendar module of python does not directly provides a function to 
#           determine the number of leap years in a given range. But we can create a small 
#           function that does this job using the isleap function of the calender module

# g. find and use a function in module calendar to determine which day of 
# the week July 29, 2016 will be 
date = 29
month = 7 # july
year = 2016
days_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday = calendar.weekday(year, month, date)
print(f"2.g. day on {date}/{month}/{year} is {days_name[weekday]}")
# solution: using the weekday function in the calendar module we can get the number of the day in this case 
#           it is 4 so we can use the list of the names to get the actual answer which would be friday 

# problem 3
# create a file named exercise.py with this code inside it:
# def average(num1: float, num2: float) -> float:
#     """Return the avergae of num1 and num2"""
#     return (num1+num2)/2
# a. run exercise.py. import doctest and run doctest.testmod()
# def average(num1: float, num2: float) -> float:
#     """Return the average of num1 and num2

#     >>> average(10, 30)
#     15.0

#     >>> average(2.5, 3.5)
#     2.75
#     """
#     return (num1 + num2) / 2

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
# solution: both the test fails in this code 

# b. both of the tests in function average's docstring fail. Fix 
# the code and rerun the tests. repeat this procedure until the tests pass.
def average(num1: float, num2: float) -> float:
    """Return the average of num1 and num2

    >>> average(10, 20)
    15.0

    >>> average(2.5, 3.0)
    2.75
    """
    return (num1 + num2) / 2

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# solution: this code will pass as both the tests will not encounter any issue

# contributed by: Jainil Jain