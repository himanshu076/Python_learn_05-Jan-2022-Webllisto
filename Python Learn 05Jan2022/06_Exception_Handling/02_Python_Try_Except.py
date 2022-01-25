'''
Errors and Exceptions in Python
Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program. 
Two types of Error occurs in python. 
 

Syntax errors
Logical errors (Exceptions) 


********************************************************************************************

Syntax errors
When the proper syntax of the language is not followed then a syntax error is thrown.
Example 
 


# initialize the amount variable
amount = 10000
  
# check that You are eligible to
#  purchase Dsa Self Paced or not
if(amount>2999)
    print("You are eligible to purchase Dsa Self Paced"

It returns a syntax error message because after the if statement a colon: is missing. We can fix this by writing the correct syntax.
 

logical errors(Exception)
When in the runtime an error that occurs after passing the syntax test is called exception or logical type. For example, when we divide any number by zero then the ZeroDivisionError exception is raised, or when we import a module that does not exist then ImportError is raised.
Example 1: 
 


# initialize the amount variable
marks = 10000
  
# perform division with 0
a = marks / 0
print(a)

'''


# Example 1:
# data = 50
# try:
#     data = data/10
# except ZeroDivisionError:
#     print('Cannot divide by 0 ', end = '')
# else:
#     print('Division successful ', end = '')
# finally:
#     print('GeeksforGeeks ', end = '')

# print(locals()['__builtins__'])
# locals()['__builtins__']


# while True:
#     data = input('Enter name : ')
#     print ('Hello  ', data)


# import math
  
# print (math.exp(1000))

# *************************************************************************************
# def my_generator():
#     try:
#         for i in range(5):
#             print ('Yielding', i)
#             yield i
#     except GeneratorExit:
#         print ('Exiting early')
  
# g = my_generator()
# print (g.__next__())
# g.close()

# help(Exception)
# help(type(self))
# help(type)


# n = int(input())
# k = int(input())
# print(n," ",k)