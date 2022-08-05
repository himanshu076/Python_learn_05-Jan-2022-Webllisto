'''Python Property Decorator - @property

A decorator feature in Python wraps in a function, appends several functionalities to existing code and then returns it. Methods and functions are known to be callable as they can be called. Therefore, a decorator is also a callable that returns callable. This is also known as metaprogramming as at compile time a section of program alters another section of the program.

Note: For more information, refer to Decorators in Python

Python @property decorator
@property decorator is a built-in decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property(). Which is used to return the property attributes of a class from the stated getter, setter and deleter as parameters.'''

# Python program to illustrate the use of property decorator
  
# Defining class
class Portal:
    # Defining __init__ method
    def __init__(self) -> None:
        self.__name = ''

    # Using @property decorator
    # @property

    # Getter method
    def name(self):
        return self.__name

    # @name.setter
    def name(self, val):
        self.__name = val

    # Deleter method
    # @name.deleter
    def name(self):
        del self.__name

# Creating Object
p = Portal()

# Setting name
p.name = 'GeeksforGeeks'

# print name
print(p.name)

# Deleting name
del p.name

# As name is deleted above this 
# will throw an erro
# print(p.name)

