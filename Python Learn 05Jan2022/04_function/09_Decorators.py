'''
Decorators
As stated above the decorators are used to modify the behaviour of function or class. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

Syntax for Decorator: 
'''

# @gfg_decorator
# def hello_decorator():
#     print("Gfg")

# # Above code is equivalent to -

# def hello_decorator():
#     print("Gfg")
    
# hello_decorator = gfg_decorator(hello_decorator)

# ********************************************************************************************
""" Chaining decorators """
# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
  
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
  
@decor1
@decor
def num():
    return 10
  
print(num())

# decor1(decor(num))  # above decorators is similar to this decorators


