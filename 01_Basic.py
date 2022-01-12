'''Python Basic'''

'''
Dictionary — A dictionary is a mutable unordered collection that Python indexes with name and value pairs.
List — A list is a mutable ordered collection that allows duplicate elements.
Set — A set is a mutable unordered collection with no duplicate elements.
Tuple — A tuple is an immutable ordered collection that allows duplicate elements.
'''

# Print statement
# print("Hello World")
# ************************************************************************

'''List'''
# nums = []

# appending data
# nums.append(10)
# nums.append(20.5)
# nums.append("string")

# print(nums)

# ************************************************************************
'''Input & Output'''
# 1.
# Name = input("Enter Your Name : ")
# print("hello!", Name)

# 2.
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = num1 * num2
# print("Product is: ", num3)

# ************************************************************************
'''Selection in Python is made using the two keywords 'if' and 'elif' and else'''

# num1 = 34
# if num1>12:
#     print("num1 is good")
# elif num1>35:
#     print("num2 is not goooooo.....")
# else:
#     print("num2 is not good")

# ************************************************************************
'''Functions'''
# 1.
# def hello():
#     print("hello")
#     print("hello again")

# hello()

# 2.
# function with main
# def getInteger():
#     result = int(input("Enter Integers: "))
#     return result

# def main():
#     print("Startet")
    
#     output = getInteger()
#     print(output)

# now we are required to tell Python 
# for 'Main' function existence
# if __name__ == "__main__":
#     main()

# ************************************************************************
'''Iteration (Looping)'''
# for step in range(5):
#     print(step)

# ************************************************************************
'''Modules'''
# import math

# def Main():
#     num = -85

    # fabs is used to get the absolute value of a decimal
#     num = math.fabs(num)
#     print(num)

# if __name__ == "__main__":
#     Main()

# ************************************************************************
'''Python keyword'''
# import keyword

# print(keyword.__annotations__)
# print(keyword.__spec__)
# print(keyword.iskeyword)
# print(keyword.issoftkeyword)
# print(keyword.softkwlist)
# print(keyword.kwlist)
# print(keyword.__builtins__)
# print(keyword.__cached__)
# print(keyword.__file__)
# print(keyword.__dict__)
# print(keyword.__loader__)
# print(keyword.__doc__)
# print(keyword.__name__)
# print(keyword.__qualname__)
# print(keyword.__path__)
# print(keyword.__package__)
# print(keyword.__all__)

# or, Not & And, is & in Keyword
# or
# print(True or False)

# And
# print(True and False)

# not
# print(not True)

# in
# if 's' in 'greeksforgreeks':
#     print("s is part of greeksforgreeks")
# else:
#     print("s is part of greeksforgreeks")

# using "in" to loop through
# for i in 'greeksforgreeks':
    # print(i, end=" ")

# print("\r")

# is
# print(' ' is ' ')
# print({} is {})

# ************************************************************************
# '''Iteration Keywords – for, while, break, continue'''

# for loop
# for i in range(10):
#     print(i, end=" ")

#     if i == 6:
#         break
# print()

# while loop
# i = 0
# while i < 10:
#     if i == 6:
#         i+= 1
#         continue
#     else:
#         print(i, end=" ")
#     i+= 1

# ************************************************************************
# '''conditional keywords - if, else, elif'''
# i = 20
# if i==10:
#     print("i is 10")
# elif i==15:
#     print("i is 20")
# else:
#     print("i is not present")

# ************************************************************************
# def - user defined function
# def fun():
#     print("Inside Function")

# fun()

# ************************************************************************
# Return keywords - Return & Yield

# return : This keyword is used to return from the function.
# yield : This keyword is used like return statement but is used to return a generator.

# return Keyword
# def fun():
#     S = 0

#     for i in range(10):
#         S += i
#         # print(S)
#     return S

# print(fun())

# Yield Keyword
# def fun():
#     S = 0

#     for i in range(10):
#         S += i
#         yield S

# for i in fun():
#     print(i)

'''Doubt'''
# def fib(limit):
    # Initialize first two Fibonacci Numbers 
    # a, b = 0, 1
    # One by one yield next Fibonacci Number
    # while a < limit:
    #     yield a
    #     a, b = b, a + b
# Create a generator object
# x = fib(5)

# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# def nextSquare():
#     i = 1
#     # An Infinite loop to generate squares
#     while True:
#         yield i*i                
#         i += 1 # Next execution resumes
#                 # from this point    
# # Driver code
# for num in nextSquare():
#     if num > 100:
#         break   
#     print(num)

# ************************************************************************
# Class

# class Dog:
#     attr1 = "mammal"
#     attr2 = "dog"

#     # A sample Method
#     def fun(self):
#         print("I'm a", self.attr1)
#         print("I'm a", self.attr2)
        
# # print(Dog().fun())
# Rodger = Dog()
# print(Rodger.attr1)
# Rodger.fun()

# ************************************************************************
# With keyword

# with open('file_path', 'w') as file:
#     file.write('hello world !')

# ************************************************************************
# as keyword
# import math as fg

# print(fg.factorial(5))

# ************************************************************************
# n = 10
# for i in range(n):
#     pass

