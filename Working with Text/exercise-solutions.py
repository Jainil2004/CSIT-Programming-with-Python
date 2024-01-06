# Question 1
"""
1. What value does each of the following expressions evaluate to? Verify your
answers by typing the expressions into the Python shell.
a. 'Computer' + ' Science'
b. 'Darwin\'s'
c. 'H2O' * 3
d. 'CO2' * 0
"""

# Answer
"""
a. Computer Science
b. Darwin
c. H2OH2OH2O
"""

# Question 2
"""
2. Express each of the following phrases as Python strings using the appropriate type of quotation marks (single, double, or triple) and, if necessary, escape sequences. There is more than one correct answer for each of these phrases.
a. They’ll hibernate during the winter.
b. “Absolutely not,” he said.
c. “He said, ‘Absolutely not,’” recalled Mel.
d. hydrogen sulfide
e. left\right
"""

# Answer
"""
a.  "They'll hibernate during the winter."
b . '"Absolutely not," he said.'
c. ""He said, 'Absolutely not,'" recalled Mel." 
d. 'hydrogen sulfide'
"""

# Question 3
"""
3. Rewrite the following string using single or double quotes instead of triple quotes:
'''A B C'''
"""

# Answer
"""
'A B C'
"""

# Question 4
"""
Use built-in function len to find the length of the empty string.
"""

# Answer
# len('')  
# Question 5
"""
5. Given variables x and y, which refer to values 3 and 12.5, respectively, use function print to print the following messages. When numbers appear in the messages, variables x and y should be used.
a. The rabbit is 3.
b. The rabbit is 3 years old.
c. 12.5 is average.
d. 12.5 * 3
e. 12.5 * 3 is 37.5.
"""

# Answer
"""
a. print(f'The rabbit is {x}.')
b. print(f'The rabbit is {x} years old.')
c. print(f'{y} is average.')
d. print(y * x)
e. print(f'{y} * {x} is {y * x}.')
"""

# Question 6
"""
6. Consider this code:
>>> first = 'John'
>>> last = 'Doe'
>>> print(last + ', ' + first)
"""

# Answer
"""
Doe, John
"""

# Question 7
"""
7. Use input to prompt the user for a number, store the number entered as a float in a variable named num, and then print the contents of num.
"""

# Answer
"""
num = float(input('Enter a number'))
print(num)
"""

# Question 8
#"""
#8. Complete the examples in the docstring and then write the body of the following function:
#def repeat(s: str, n: int) -> str:
 #   """ Return s repeated n times; if n is negative, return the empty string.
  #    >>> repeat('yes', 4)
   #     'yesyesyesyes'
    #    >>> repeat('no', 0)
     #   >>> repeat('no', -2)
      #  >>> repeat('yesnomaybe', 3)
   # """
"""

# Answer
"""
def repeat(s: str, n: int) -> str:
    """Return s repeated n times; if n is negative, return the empty string.
    
    Examples:
    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    ''
    >>> repeat('no', -2)
    ''
    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'
    """
    if n < 0:
        return ''
    else:
        return s * n
"""

# Question 8
"""
9.# Complete the examples in the docstring and then write the body of the following function:
def total_length(s1: str, s2: str) -> int:
    """ Return the sum of the lengths of s1 and s2.
        >>> total_length('yes', 'no')
        5
        >>> total_length('yes', '')
        >>> total_length('YES!!!!', 'Noooooo')
    """
"""

# Answer
"""
def total_length(s1: str, s2: str) -> int:
    """Return the sum of the lengths of s1 and s2.
    
    Examples:
    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')
    3
    >>> total_length('YES!!!!', 'Noooooo')
    12
    """
    return len(s1) + len(s2)
