
# 1.
# def myFun(*args,**kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)
 
 
# # Now we can use both *args ,**kwargs
# # to pass arguments to this function :
# myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")

# **************************************************************************************
# 2.
# A generator function that yields 1 for the first time, 2 second time and 3 third time
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
  
# # Driver code to check above generator function
# for value in simpleGeneratorFun(): 
#     print(value)

# def create_adder(x):
#     def adder(y):
#         return x+y
  
#     return adder
  
# add_15 = create_adder(15)
  
# print (add_15(10))
# print((create_adder(50))(20))
# print(create_adder(50)(20))

# *****************************************************************************************


# defining a decorator
def hello_decorator(func):
 
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
         
    return inner1
 
def function_to_be_used():
    print("This is inside the function !!")

function_to_be_used = hello_decorator(function_to_be_used)
 
function_to_be_used()