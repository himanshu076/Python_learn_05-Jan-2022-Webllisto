'''*******************************Exceptions_Errors*****************************'''

'''Base classes
The following exceptions are used mostly as base classes for other exceptions.
'''
'''1. exception BaseException
        args
        with_traceback(tb)
'''

'''2. exception Exception ---All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also
be derived from this class.
'''



'''
3. exception ArithmeticError - error due to math error.

3.1 OverflowError - Definition**
                        In Python, OverflowError occurs when any operations like arithmetic operations or any other variable storing any value above its limit then there occurs an overflow of values that will exceed it’s specified or already defined limit. In general, in all programming languages, this overflow error means the same. In Python also this error occurs when an arithmetic operation result is stored in any variable where the result value is larger than any given data type like float, int, etc exceeds the limit or value of current Python runtime values. Therefore when these values are larger than the declared data type values will result to raise memory errors.
'''
# Example 1:
# print("Simple program for showing overflow error")
# print("\n")
# import math
# print("The exponential value is")
# print(math.exp(1000))

# Example 2:
# print("Simple program for showing overflow error")
# print("\n")
# import math
# try:
#     print("The exponential value is")
#     print(math.exp(1000))
# except OverflowError as oe:
#     print("After overflow", oe)

'''3.2 ZeroDivisionError --- Definition**
                                In simple term in any arithmetic operation when value divided by zero then in Python throw ZeroDivisionError.
'''
# Example 1:
# num_list=[]
# total=0
# try
#     avg=total/len(num_list)
#     print("Average:"+avg)
# except ZeroDivisionError:
#     print ("Zero Division Error occurred")


'''3.3 FloatingPointError --- Definition**'''
                                


# import syserror

# import math
# # import fpectl
# # try:
# print('Control off:', math.exp(700))
#     # fpectl.turnon_sigfpe()
# print('Control on:', math.exp(1000))
# # except Exception as e:
# #     print(e)
#     # print(sys.__exc_type__)


'''4. exception BufferError --- Defination**
                                    Raised when a buffer related operation cannot be performed.'''
                


'''5. exception ValueErroe --- '''
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


'''6. i/oError - input output Error'''

# import sys
# def something():
#     try:
#         file = open ( "filethatdoesnotexist.txt", 'r' )
#     except IOError as e:
#         print(e)
#         # print(sys.exc_type)

# something()

'''7. EOF error - End of file'''

#try and except blocks are used to catch the exception
#EOFError program
#try and except blocks are used to catch the exception
# try:
#     while True:
# #input is assigned to a string variable check
#         check = input('The input provided by the user is being read which is:')
# #the data assigned to the string variable is read
#         print('Hello', check)
# #EOFError exception is caught and the appropriate message is displayed
# except EOFError as x:
#     print(x)

'''8. NoImplemented error'''

# class BaseClass(object):
#     def __init__(self):
#         super(BaseClass, self).__init__()
#     def do_something(self):
#         raise NotImplementedError(self.__class__.__name__ + '.try_something')
# class SubClass(BaseClass):
#     def do_something(self):
#         print (self.__class__.__name__ + ' trying something!')
#         SubClass().do_something()
#         BaseClass().do_something()

# try:
#     salary = int(input("Enter salary: "))
#     print("So cool you earn %d amount." % salary)
# except ValueError:
#     print("Hey, that wasn't a number!")

'''9. value error'''

# list = [[1,2],[3,4],[5,6],[7,8],9] 
# a,b,c = list
# print(a)
# print(b)
# print(c)

Exception