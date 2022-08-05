'''Constructors in Python
Prerequisites: Object-Oriented Programming in Python, Object-Oriented Programming in Python | Set 2 
Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.
Syntax of constructor declaration : '''
# # syntex
# def __init__(self):
#     # body of the constructor

'''
Types of constructors : 

default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.
parameterized constructor: constructor with parameters is known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

Example of default constructor :'''
# class greeksforGreeks:
#     # default constructor
#     def __init__(self) -> str:
#         self.greek = "GreeksforGreeks"

#     # a method for printing data method
#     def print_greek(self):
#         print(self.greek)

# # creating object for class
# obj = greeksforGreeks()

# # calling the instance method using the object obj
# obj.print_greek()

'''Example of the parameterized constructor : '''
class Addition:
    # class variable
    first = 0
    second = 0
    answer = 0

    # Parameterized constructer
    def __init__(self, f, s) -> str:
        self.first = f
        self.second = s

    def display(self):
        print("first number = " + str(self.first))
        print("second number = " + str(self.second))
        print("Addition of two number = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second
 
# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()
 
# display result
obj.display()