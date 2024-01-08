# exercise-solutions of Making Choices

# problem 1
print(f"\nproblem 1")
# what value does each expression produce? Verify your answers by typing the
# expressions into Python.
# a. True and not False
print(f"a. {True and not False}")

# b. True and not False
print(f"b. {True and not False}")

# c. True or True and False
print(f"c. {True or True and False}")

# d. not True or not False
print(f"d. {not True or not False}")

# e. True and not 0
print(f"e. {True and not 0}")

# f. 52 < 52.3
print(f"f. {52 < 52.3}")

# g. 1 + 52 < 52.3
print(f"g. {1 + 52 < 52.3}")

# h. 4 != 4.0
print(f"h. {4 != 4.0}")

# problem 2
print(f"\nproblem 2")
# Variables x and y refer to Boolean values.
# a. write an expression that produces true iff both variables are true.
x = True
y = True
if x and y:
    print(f"a. {x and y}")

# b. write an expression that produces ture iff x is False
x = False # this will make the code below return True
if not x:
    print(f"b. {not x}")

# c. write an exression that produceds ture iff at least one of the 
#    variables is true
if x or y:
    print(f"c. {x or y}") 

# problem 3
print(f"\nproblem 3")
# variables full and empty refer to Boolean values. write an expression that
# produces True if and only if at most one of the variables is true.
full = True
empty = False
if full != empty: # condition is only ture if either of full or empty is true
    print(f"{full != empty}")

# problem 4
print(f"\nproblem 4")
# you want an automatic wildlife camera to switch on if the light level is 
# less than 0.01 lux or if te temperature is above freezing. but not if both
# conditions are turn (you should assume that function turn_camera_on has
# already been defined)
# your first attempt to write this is as follows: 
# if (light < 0.01) or (temperature > 0):
#    if not ((light < 0.01) and (temperature > 0)):
#         turn_camera_on()
# a firend says that this is an exclusive or and that you could write it 
# more simply as follows:
# if (light < 0.01) != (temperature > 0):
#     turn_camera_on()
# is your friend right? if so, explain why. if not, give values for light
# and temperature that will produce different results for the two fragments of code

# solution: the friend is right both the codes work the same way but the
# second code is more efficient and easier to read. the first code is
# unnecessarily complicated and hard to read. so yes the first code can
# be written more simply as the second code.

# problem 5
print(f"\nproblem 5")
# In Functions that python provides, on page 31, we saw built-in function
# abs. Variable x refer to a number. write an expression that evaluates to 
# True if x and its absolute value are equal and evaluates to False otherwise.
# Assign the resulting value to a variable named result.
result = False
x = 5
if x == abs(x):
    result = True
print(f"result = {result}")

# problem 6
print(f"\nproblem 6")
# write a function named different that has two parameters, a and b. the function
# should return True if a and b refer to different values and should return
# false otherwise.
def different(a, b):
    return a != b

print(f"different(5, 5) = {different(5, 4)}") # this will return true
print(f"different(5, 5) = {different(5, 5)}") # this will return false

# problem 7
print(f"\nproblem 7")
# Variables population and land_area refer to floats.
# a. write an if statement that will print the population if it is less than
# 10,000,000
population = 500000
if population < 10000000:
    print(f"population = {population}")

# b. write an if statement that will print the population if it is between 
# 10,000,000 and 35,000,000
population = 20000000
if population > 10000000 and population < 35000000:
    print(f"population = {population}")

# c. write an if statement that will print "Densely Populated" if the land
# density (number of people per unit of area) is greater than 100
land_area = 10000
if population / land_area > 100:
    print(f"Densely Populated")

# d. write an if statement that will print "Densely Populated" if the land
# density is greater than 100 and "Sparsely Populated" otherwise
land_area = 1000000
if population / land_area > 100:
    print(f"Densely Populated")
else:
    print(f"Sparsely Populated")

# problem 8
print(f"\nproblem 8")
# function convert_to_celsius from defining our own functions, on page 35,
# converts from Fahrenheit to Celsius. wikipedia, however, discusses eight 
# temperature scales: kelvin, Celsius, Fahrenheit, Rankine, Delisle, Newton, 
# Réaumur, and Rømer
# a. write a convert_temperatures(t, source, target) function that converts
# temperature t from source units to target units, where source and target are 
# each one of "Kelvin", "Celsius", "Fahrenheit", "Rankine", "Delisle", "Newton",
# "Réaumur", and "Rømer" units
# a better way is to choose one canonical scale, such as celcius. Your 
# conversion functions could work in two steps: convert form the source 
# scale to Celsius and then from celsius to the target scale.

def convert_temperature(t, source, target):
    # conversion into celsius scale from source scale
    if source.lower() == 'celsius':
        temp_in_celsius = t
    elif source.lower() == 'fahrenheit':
        temp_in_celsius = (t - 32) * 5/9
    elif source.lower() == 'kelvin':
        temp_in_celsius = t - 273.15
    elif source.lower() == 'rankine':
        temp_in_celsius = (t - 491.67) * 5/9
    elif source.lower() == 'delisle':
        temp_in_celsius = 100 - t * 2/3
    elif source.lower() == 'newton':
        temp_in_celsius = t * 100/33
    elif source.lower() == 'reaumur':
        temp_in_celsius = t * 5/4
    elif source.lower() == 'romer':
        temp_in_celsius = (t - 7.5) * 40/21

    # convserion into target scale
    if target.lower() == 'celsius':
        result_temp = temp_in_celsius
    elif target.lower() == 'fahrenheit':
        result_temp = (temp_in_celsius * 9/5) + 32
    elif target.lower() == 'kelvin':
        result_temp = temp_in_celsius + 273.15
    elif target.lower() == 'rankine':
        result_temp = (temp_in_celsius + 273.15) * 9/5
    elif target.lower() == 'delisle':
        result_temp = (100 - temp_in_celsius) * 3/2
    elif target.lower() == 'newton':
        result_temp = temp_in_celsius * 33/100
    elif target.lower() == 'reaumur':
        result_temp = temp_in_celsius * 4/5
    elif target.lower() == 'romer':
        result_temp = (temp_in_celsius * 21/40) + 7.5

    return result_temp

# b. now if you added a new temperatur scale, how many if
# statements would you need to add?

# solution: if we add only if statements then we would need 8 new if statements
# but if we use elif statements then we would need only 1 new elif statement

# problem 9
print(f"\nproblem 9")
# assume we want to print a string warning message if a pH value is below
# 3.0 and otherwise simply report on the acidity. we tru this if statement:
ph = 2
if ph < 7.0:
    print(ph ,"It's acidic!")
elif ph < 3.0:
    print(ph, "is VERY acidic ! Be careful.")
# this prints the wrong message when a ph of 2 is entered. what is the 
# problem and how can you fix it?

# solution: the problem is that if the first statement is true then the second
# statement will not be checked. as elif works in a way that if the first
# statement is false only then check the elif statement. so we can fix it by
# changing the elif statement to if statement. corrected code: 
if ph < 7.0:
    print(ph ,"It's acidic!")
if ph < 3.0: # elif changed to if
    print(ph, "is VERY acidic ! Be careful.")

# problem 10
print(f"\nproblem 10")
# the following code displays a messages about the acidity of a solution:
ph = float(input("Enter the pH level: "))
if ph < 7.0:
    print("It's acidic!")
elif ph < 4.0: 
    print("its a strong acid!")

# a. what message are displayed when the user enters 6.4?
# solution: the output will be "It's acidic!"
# b. what message are displayed when the user enters 3.6?
# c. make a small change to one line of code so that both messages are 
# displayed when a value less than 4 is entered
# solution: change the elif statement to if statement

ph = float(input("Enter the pH level: "))
if ph < 7.0:
    print("It's acidic!")
if ph < 4.0: # elif changed to if
    print("its a strong acid!")

# problem 11
# why does the last example in remembering reults of a Boolean Expression
# Evaluation, on page 92, check to see whether someone is light rather 
# than heavy if you wanted to write the second assignment statements as 
# heavy = bmi >= 22.0, what changes would you have to make to the code?

# solution: the last example checks to see whether someone is light rather
# than heavy because the if statement is written in a way that if the first
# condition is true then the second condition will not be checked. so if we
# want to write the second assignment statement as heavy = bmi >= 22.0 then
# we would have to change the if statement to elif statement. corrected code:
bmi = 21.7
if bmi < 22.0:
    print("BMI is", bmi)
elif bmi >= 22.0:
    print("you are heavy.")

# contributed by: Jainil Jain
