import math

#A module is a collection of variables and functions. The math module provides a variable called pi that contains the value of the mathematical constant denoted 
#. We can display its value like this. 

print(math.pi)
print(math.sqrt(25))
print(math.pow(5, 2))
round(2.5)

def add(a, b):
    return a + b


def power(a, b):
    return math.pow(a, b)













# import eines gesamten moduls
import math
print(math.sqrt(16))

# import einer spezifischen funktion
from math import sqrt
print(sqrt(16))
