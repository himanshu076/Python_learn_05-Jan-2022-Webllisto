'''Syntax: 
1.*************************************************************************************
def function_name(parameters):
    """docstring"""
    statement(s)
    return expression
    
2. ************************************************************************************
Example: Python Calling Function
# A simple Python function
def fun():
  print("Welcome to GFG")
         
# Driver code to call a function
fun()
    
3. ************************************************************************************
Python Function with arguments
In this example, we will create a simple function to check whether the number passed as an argument to the function is even or odd 
def evenodd():
    if (x % 2) == 0:
        print("Even")
    else:
        print("Odd")

# Driver code to call the function
evenodd(2)
evenodd(3)


----------------------------Types of Arguments---------------------------
4.*************************************************************************************
Python supports various types of arguments that can be passed at the time of the function call. Let's discuss each type in detail.

*****************4.1  Default arguments
A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument. The following example illustrates Default arguments. 

# Python program to demonstrate
# default arguments
  
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
 
# Driver code (We call myFun() with only
# argument)
myFun(10)

*****************4.2 Keyword arguments
The idea is to allow the caller to specify the argument name with values so that caller does not need to remember the order of parameters.


# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
 

# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')

*****************4.3 Variable-length arguments
In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:

*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)

*****************4.3.1 Example 1: Variable length non-keywords argument

# Python program to illustrate
# *args for variable number of arguments
 
 
def myFun(*argv):
    for arg in argv:
        print(arg)
 
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

*****************4.3.2 Example 2: Variable length keyword arguments

# Python program to illustrate
# *kwargs for variable number of keyword arguments
 
 
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

5. *********************************************************************************
Docstring -------------
The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.

The below syntax can be used to print out the docstring of a function:

Syntax: print(function_name.__doc__)    -///////////////////////

Example: Adding Docstring to the function

# A simple Python function to check
# whether x is even or odd
 
 
def evenOdd(x):
    """Function to check if the number is even or odd"""
     
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
 
# Driver code to call the function
print(evenOdd.__doc__)

6. ********************************************************************************
The return statement ---------------
The function return statement is used to exit from a function and go back to the function caller and return the specified value or data item to the caller.

Syntax: return [expression_list]
The return statement can consist of a variable, an expression, or a constant which is returned to the end of the function execution. If none of the above is present with the return statement a None object is returned.

Example: Python Function Return Statement

def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2
 
 
print(square_value(2))
print(square_value(-4))

7. ************************************************************************************
Is Python Function Pass by Reference or pass by value? -------------
One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function, a new reference to the object is created. Parameter passing in Python is the same as reference passing in Java.

Example:


# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20
 
 
# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

8. ****************************************************************************************
Anonymous functions: -------------
In Python, an anonymous function means that a function is without a name. As we already know the "def" keyword is used to define the normal functions and the "lambda" keyword is used to create anonymous functions. Please see this for details.

# Python code to illustrate the cube of a number
# using lambda function
 
 
def cube(x): return x*x*x
 
cube_v2 = lambda x : x*x*x
 
print(cube(7))
print(cube_v2(7))

9. *****************************************************************************************
Python Function within Functions ------------
A function that is defined inside another function is known as the inner function or nested function. Nested functions are able to access variables of the enclosing scope. Inner functions are used so that they can be protected from everything happening outside the function.

# Python program to
# demonstrate accessing of
# variables of nested functions
 
def f1():
    s = 'I love GeeksforGeeks'
     
    def f2():
        print(s)
         
    f2()
 
# Driver's code
f1()





    
    '''

