'''
Global and Local Variables in Python
 
Global variables are those which are not defined inside any function and have a global scope whereas local variables are those which are defined inside a function and its scope is limited to that function only. In other words, we can say that local variables are accessible only inside the function in which it was initialized whereas the global variables are accessible throughout the program and inside every function


1. **********************************************************************************
Local Variables --------------
Local variables are those which are initialized inside a function and belongs only to that particular function. It cannot be accessed anywhere outside the function. Lets see how to create a local variable.

Example: Creating local variables
def f():
     
    # local variable
    s = "I love Geeksforgeeks"
    print(s)
 
# Driver code
f()

2. **************************************************************************************
Global Variables ------------
The global variables are those which are defined outside any function and which are accessible throughout the program i.e. inside and outside of every function Let’s see how to create a global variable.

Example: Defining and accessing global variables


# This function uses global variable s
def f():
    print("Inside Function", s)
 
# Global scope
s = "I love Geeksforgeeks"
f()
print("Outside Function", s)





'''
