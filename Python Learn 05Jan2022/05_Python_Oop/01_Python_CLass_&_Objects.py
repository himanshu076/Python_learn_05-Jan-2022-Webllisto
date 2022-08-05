# class before:
#     att1 = "kishor"
#     att2 = "Dinesh"

#     def func(self):
#         print("I'm a", self.att1 )
#         print("I'm a", self.att2 )

# Rodger = before()

# print(Rodger.att1)
# Rodger.func()

'''The self
Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it.
If we have a method that takes no arguments, then we still have to have one argument.
This is similar to this pointer in C++ and this reference in Java.
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.'''

# ************************************************************************************

'''__init__ method
The __init__ method is similar to constructors in C++ and Java. Constructors are used to initializing the object’s state. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It runs as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
'''
# A class with init Method:
# class person():

#     # init method constructor
#     def __init__(self, name) -> str:
#         self.name = name

#     # Sample Method
#     def say_hi(self):
#         print("Hello, my name is", self.name)

# p = person("kishor")
# p.say_hi()


'''Class and Instance Variables
Instance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class. Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables are variables whose value is assigned in the class.

Defining instance variable using a constructor. '''
'''Example 1:'''
# class for dog
# class dog:
#     # class variable
#     animal = 'dog'

#     # The init method or constructor
#     def __init__(self, breed, color) -> str:
#         # Instance variable
#         self.breed = breed
#         self.color = color

# Rodger = dog("pug", "Brown")
# Buzo = dog("Bulldog", "Black")

# print("Rodger details: ")
# print('Rodger is a',  Rodger.animal)
# print('Breed: ', Rodger.breed)
# print('color: ', Rodger.color)

# print("Buzo details: ")
# print('Buzo is a',  Buzo.animal)
# print('Breed: ', Buzo.breed)
# print('color: ', Buzo.color)

'''Example 2:'''
# Class for dog
class Dog:
    # class variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed) -> str:
        # Instance variable
        self.breed = breed
    
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

# Drive code
Rodger = Dog('pug')
Rodger.setColor('brown')
print(Rodger.getColor())
