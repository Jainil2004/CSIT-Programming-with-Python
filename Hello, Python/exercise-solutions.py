# exercise-solutions of Hello, Python

# problem 1
print(f"\nproblem 1")
# for each fo the following expressions, what value will the expression give? Verify your answers by typing the expressions into the Python.
# a. 9 - 3
print(f"a. {9 - 3}")

# b. 8 * 2.5
print(f"b. {8 * 2.5}")

# c. 9 / 2
print(f"c. {9 / 2}")

# d. 9 / -2
print(f"d. {9 / -2}")

# e. 9 // -2
print(f"e. {9 // -2}")

# f. 9 % 2
print(f"f. {9 % 2}")

# g. 9.0 % 2
print(f"g. {9.0 % 2}")

# h. 9 % 2.0
print(f"h. {9 % 2.0}")

# i. 9 % -2
print(f"i. {9 % -2}")

# j. -9 % 2
print(f"j. {-9 % 2}")

# k. 9 / -2.0
print(f"k. {9 / -2.0}")

# l. 4 + 3 * 5
print(f"l. {4 + 3 * 5}")

# m. (4 + 3) * 5
print(f"m. {(4 + 3) * 5}")

# problem 2
print(f"\nproblem 2")
# unary minus negates a number, Unary plus exists as well; for example,
# python understands +5. if x has the value -17, what do you think +x
# should do? shwould it leave the sign of the number alone? should it act
# like absoulte value, removing any negatio? Use the Python shell to find
# out its behavior.

x = -17
print(f"x = {x}")
print(f"+x = {+x}")
# Solution: it leaves the sign of the number alone and does not act like absolute value or change anything.

# problem 3
print(f"\nproblem 3")
# Write two assignments statements that do the following:
# a. create a new variable, temp, and assign it the value 24.
# b. convert the value in temp from Celsius to Fahrenheit by multiplying
#    by 1.8 and adding 32; make temp refer to the resulting value.
# what is the temp's new value?

temp = 24
temp = temp * 1.8 + 32
print(f"temp in Celsius = 24, temp in Fahrenheit = {temp}")
# Solution: temp's new value is 75.2 after performing the calculation

# problem 4
print(f"\nproblem 4")
# for each of the following expressions, in which order are the 
# subexpressions evaluated?
# a. 6 * 3 + 7 * 4
print(f"a. {6 * 3 + 7 * 4}")

# b. 5 + 3 / 4
print(f"b. {5 + 3 / 4}")

# c. 5 - 2 * 3 ** 4
print(f"c. {5 - 2 * 3 ** 4}")

# solution: python follows the order of operations, which is PEMDAS
#           PEMDAS: Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
#           the priority of the operators is as follows: **, *, /, +, -

# problem 5
print(f"\nproblem 5")
# a. create a new variable x, and assign it the value 10.5
# b. create a new variable y, and assign it the value 4.
# c. sum x and ym and make x refer to the resulting value. After this statement
#    is executed, what are the values of x and y?

x = 10.5
y = 4
x = x + y
print(f"x = {x}, y = {y}")
# Solution: x = 14.5, y = 4, the value of x is modified from 10.5 to 14.5
#           the value of y remains the same

# problem 6
print(f"\nproblem 6")
# write a bullet list description of what happens when python evaluates
# the statement x += x - x when x has the value 3

x = 3
x += x - x
print(f"x = {x}")
# Solution: x += x - x is equivalent to x = x + (x - x) hence giving x = 3

# problem 7
# print(f"\nproblem 7")
# when a variable is used before it has been assigned a value, a NameError
# occurs. in the Python shell, write an expression that results in a NameError
# var1
# print(var1)
# Solution: uncomment the above line to see the NameError
#           we have not assigned any value to var1, hence the NameError

# problem 8
print(f"\nproblem 8")
# which of the following expressions results in SyntaxErrors?
# a. 6 * -----5
print(f"a. {6 * -----5}") 

# b. 8 = people
# 8 = people -- SyntaxError: cannot assign to literal

# c. ((((4 ** 3))))
print(f"c. {((((4 ** 3))))}")

# d. (-(-(-(-5))))
print(f"d. {(-(-(-(-5))))}")

# e. 4 += 7 /2
# 4 += 7 /2 -- SyntaxError: invalid syntax 

# contributed by: Jainil Jain