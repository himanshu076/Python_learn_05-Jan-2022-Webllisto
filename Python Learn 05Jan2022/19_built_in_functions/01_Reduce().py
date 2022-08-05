'''reduce() in Python
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.'''

import functools
import itertools
import numbers
import operator
import re


list1 = [20,30,40,50,60,70,80,90]

# print("Sum of all num :", functools.reduce(lambda a,b : a+b, list))

# print("Maximum Number : ", functools.reduce(lambda a,b : a if a>b else b, list))

# *************************************************************************************
'''Using Operator Functions
reduce() can also be combined with operator functions to achieve the similar functionality as with lambda functions and makes the code more readable.'''

# print("sum of all elements :", functools.reduce(operator.mul, list1))
# print("sum of all elements :", functools.reduce(operator.mod, list1))
# print("sum of all elements :", functools.reduce(operator.add, list1))
# print("sum of all elements :", functools.reduce(operator.add, ["greeks ", "for ", "greeks "]))

'''******************accumulate******************'''
from itertools import accumulate

# print("Summation of list using accumulate is : ", end="")
# print(list(itertools.accumulate(list1, lambda x,y : x+y)))

# print("The summation of list using reduce is : ", end="")
# print(functools.reduce(lambda x,y : x+y, list1))


'''Reduce function i.e. reduce() function works with 3 parameters in python3 as well as for 2 parameters. To put it in a simple way reduce() places the 3rd parameter before the value of the second one, if it' s present. Thus, it means that if the 2nd argument is an empty sequence, then 3rd argument serves as the default one. 

 Here is an example :(This example has been take from the  functools.reduce() documentation includes a Python version of the function:'''

# def reduce(func, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
    
#     for elem in it:
#         value = func(value, elem)
#     return value

# list = [3,4,5,6,2,7,8,9]
# print(reduce(lambda x, y: x+y, list, 6))


'''reduce function using function'''

# def my_add(a, b):
#     return a + b

# from functools import reduce

# numbers = [1, 2, 3, 5, 7, 4]
# a = reduce(my_add, numbers, 40)
# print(a)

