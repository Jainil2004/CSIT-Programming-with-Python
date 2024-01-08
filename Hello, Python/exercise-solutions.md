# Exercise Solutions of Hello, Python

## Problem 1

For each fo the following expressions, what value will the expression give? Verify your answers by typing the expressions into the Python.

```python
# Code
print(f"a. {9 - 3}")
print(f"b. {8 * 2.5}")
print(f"c. {9 / 2}")
print(f"d. {9 / -2}")
print(f"e. {9 // -2}")
print(f"f. {9 % 2}")
print(f"g. {9.0 % 2}")
print(f"h. {9 % 2.0}")
print(f"i. {9 % -2}")
print(f"j. {-9 % 2}")
print(f"k. {9 / -2.0}")
print(f"l. {4 + 3 * 5}")
print(f"m. {(4 + 3) * 5}")

# Output
a. 6
b. 20.0
c. 4.5
d. -4.5
e. -5
f. 1
g. 1.0
h. 1.0
i. -1
j. 1
k. -4.5
l. 60
m. 35
```

## Problem 2

Unary minus negates a number, Unary plus exists as well; for example, python understands +5. if x has the value -17, what do you think +x should do? shwould it leave the sign of the number alone? should it act like absoulte value, removing any negatio? Use the Python shell to find out its behavior.

```python
# Code
x = -17
print(f"x = {x}")
print(f"+x = {+x}")

# Output
x = -17
+x = -17
```

## Problem 3

Write two assignments statements that do the following:    a. create a new variable, temp, and assign it the value 24. b. convert the value in temp from Celsius to Fahrenheit by multiplying by 1.8 and adding 32; make temp refer to the resulting value.
What is the temp's new value?

```python
# Code
temp = 24
temp = temp * 1.8 + 32
print(f"temp in Celsius = 24, temp in Fahrenheit = {temp}")
# Solution: temp's new value is 75.2 after performing the calculation

# Output
temp in Celsius = 24, temp in Fahrenheit = 75.2
```

## Problem 4

For each of the following expressions, in which order are the subexpressions evaluated?

```python
# Code
print(f"a. {6 * 3 + 7 * 4}")
print(f"b. {5 + 3 / 4}")
print(f"c. {5 - 2 * 3 ** 4}")
# solution: python follows the order of operations, which is PEMDAS
#           PEMDAS: Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
#           the priority of the operators is as follows: **, *, /, +, -

# Output
a. 46
b. 5.75
c. -157
```

## Problem 5

a. create a new variable x, and assign it the value 10.5
b. create a new variable y, and assign it the value 4.
c. sum x and ym and make x refer to the resulting value.
After this statement is executed, what are the values of x and y?

```python
# Code
x = 10.5
y = 4
x = x + y
print(f"x = {x}, y = {y}")
# Solution: x = 14.5, y = 4, the value of x is modified from 10.5 to 14.5
#           the value of y remains the same

# Output
x = 14.5, y = 4
```

## Problem 6
Write a bullet list description of what happens when python evaluates the statement x += x - x when x has the value 3

```python
# Code
x = 3
x += x - x
print(f"x = {x}")
# Solution: x += x - x is equivalent to x = x + (x - x) hence giving x = 3

# Output
x = 3
```

## Problem 7
When a variable is used before it has been assigned a value, a NameError occurs. in the Python shell, write an expression that results in a NameError

```python
# Code
var1
print(var1)

# Output for var1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'var1' is not defined. Did you mean: 'vars'?

# Output for print(var1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'var1' is not defined. Did you mean: 'vars'?
```

## Problem 8

Which of the following expressions results in SyntaxErrors?

```python
# Code
print(f"a. {6 * -----5}")
# b. 8 = people
# 8 = people -- SyntaxError: cannot assign to literal
print(f"c. {((((4 ** 3))))}")
print(f"d. {(-(-(-(-5))))}")
# e. 4 += 7 /2
# 4 += 7 /2 -- SyntaxError: invalid syntax

# Output
a. -30
c. 64
d. 5
```

*Made with help of Jainil Jain*