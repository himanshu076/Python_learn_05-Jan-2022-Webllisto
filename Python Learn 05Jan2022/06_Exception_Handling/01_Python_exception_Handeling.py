'''Error Examples'''
'''Example 1: '''
# Python program to handle simple runtime error
#Python 3
 
# a = [1, 2, 3]
# try:
#     print ("Second element = %d" %(a[1]))
 
#     # Throws error since there are only 3 elements in array
#     print ("Fourth element = %d" %(a[3]))
 
# except:
#     print ("An error occurred")

'''Example 2:'''
# Program to handle multiple errors with one
# except statement
# Python 3
 
# def fun(a):
#     if a < 4:
 
#         # throws ZeroDivisionError for a = 3
#         b = a/(a-3)
 
#     # throws NameError if a >= 4
#     print("Value of b = ", b)
     
# try:
#     fun(3)
#     fun(5)
 
# # note that braces () are necessary here for
# # multiple exceptions
# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")
# except NameError:
#     print("NameError Occurred and Handled")

'''Example 3:'''

# Try with Else Clause
# In python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters the else block only if the try clause does not raise an exception.

# Example: Try with else clause


# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
# def AbyB(a , b):
#     try:
#         c = ((a+b) / (a-b))
#     except ZeroDivisionError:
#         print ("a/b result in 0")
#     else:
#         print (c)
 
# # Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

'''Example 4:'''

# Finally Keyword in Python
# Python provides a keyword finally, which is always executed after the try and except blocks. The final block always executes after normal termination of try block or after try block terminates due to some exception.

# Syntax:

# try:
#     # Some Code.... 

# except:
#     # optional block
#     # Handling of exception (if required)

# else:
#     # execute if no exception

# finally:
#     # Some code .....(always executed)
# Example:


# Python program to demonstrate finally
 
# No exception Exception raised in try block
# try:
#     k = 5//0  # raises divide by zero exception.
#     print(k)
 
# # handles zerodivision exception
# except ZeroDivisionError:
#     print("Can't divide by zero")
 
# finally:
#     # this block is always executed
#     # regardless of exception generation.
#     print('This is always executed')


def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e
  
example()