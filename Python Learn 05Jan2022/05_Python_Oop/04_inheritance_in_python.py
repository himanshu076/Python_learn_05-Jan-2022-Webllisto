'''Inheritance in Python
Inheritance is the capability of one class to derive or inherit the properties from another class. The benefits of inheritance are: 
 

It represents real-world relationships well.
It provides reusability of a code. We don't have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
Below is a simple example of inheritance in Python '''

# A Python program to demonstrate inheritance 
   
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)"

# class Person(object):
#     # Constructor
#     def __init__(self, name) -> str:
#         self.name = name

#     # To get name
#     def getName(self):
#         return self.name

#     # To check if this person is employee
#     def isEmployee(self):
#         return False

# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):
#     # Here we return True
#     def isEmployee(self):
#         return True

# emp = Person('Greek1')
# print(emp.getName(), emp.isEmployee())

# emp = Employee("Greek2")
# print(emp.getName(), emp.isEmployee())

'''What is object class? 
Like Java Object class, in Python (from version 3.x), object is root of all classes. 
In Python 3.x, “class Test(object)” and “class Test” are same. 
In Python 2.x, “class Test(object)” creates a class with object as parent (called new style class) and “class Test” creates old style class (without object parent). Refer this for more details.

Subclassing (Calling constructor of parent class) 
A child class needs to identify which class is its parent class. This can be done by mentioning the parent class name in the definition of the child class. 
Eg: class subclass_name (superclass_name): '''


# Python code to demonstrate how parent constructors
# are called.
  
# parent class
# class person(object):
#     # __init__ is known as constructor
#     def __init__(self, name, idnumber) -> str:
#         self.name = name
#         self.idnumber = idnumber
#     def display(self):
#         print(self.name)
#         print(self.idnumber)

# # child class
# class Employee(person):
#     def __init__(self, name, idnumber, salary, post) -> str:
#         # super().__init__(name, idnumber)
#         self.salary = salary
#         self.post = post

#         # invoking the __init_ of the parent class
#         person.__init__(self, name, idnumber)

# a = Employee('Rahul', 886012, 200000, "Intern")

# a.display()
        
'''Example 2: '''
# Python program to demonstrate error if we
# forget to invoke __init__() of the parent.
  
# class A:
#       def __init__(self, n = 'Rahul'):
#               self.name = n
# class B(A):
#     def __init__(self, roll):
#         self.roll = roll
        
  
# object = B(23)
# print (object.name)

'''Different forms of Inheritance: 
1. Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
2. Multiple inheritance: When a child class inherits from multiple parent classes, it is called multiple inheritance. 
Unlike Java and like C++, Python supports multiple inheritance. We specify all parent classes as a comma-separated list in the bracket. '''
# Python example to show the working of multiple 
# inheritance
# class Base1(object):
#     def __init__(self) -> None:
#         self.str1 = "Geek1"
#         print('Base1')

# class Base2(object):
#     def __init__(self) -> None:
#         self.str2 = "Geek2"
#         print('Base2')

# class Drived(Base1, Base2):
#     def __init__(self) -> None:
#         # Calling constructors of Base1 and Base2 classes
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print('Derived')

#     def printStrs(self):
#         print(self.str1, self.str2)

# ob = Drived()
# ob.printStrs()
'''3. Multilevel inheritance: When we have a child and grandchild relationship.'''
# A Python program to demonstrate inheritance 
  
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)"
# class Base(object):
#     # constructor
#     def __init__(self, name) -> str:
#         self.name = name

#     # To get name
#     def getName(self):
#         return self.name

#     # Inherited or Sub class (Note Person in bracket)
# class Child(Base):
#     # constructor
#     def __init__(self, name, age) -> str:
#         Base.__init__(self, name)
#         self.age = age

#     # To get age
#     def getAge(self):
#         return self.age

# # Inherited or Sub class (Note Person in bracket)
# class GrandChild(Child):
#     '''This is grandChild Class'''
#     # Constructor
#     def __init__(self, name, age, address) -> str:
#         Child.__init__(self, name, age)
#         self.address = address

#     # To get address
#     def getAddress(self):
#         return self.address

# # Drive mode
# g = GrandChild("Geek1", 23, "Noida")
# print(g.getName(), g.getAge(), g.getAddress())

'''4. Hierarchical inheritance More than one derived classes are created from a single base.

5. Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.

Private members of parent class 
We don’t always want the instance variables of the parent class to be inherited by the child class i.e. we can make some of the instance variables of the parent class private, which won’t be available to the child class. 
We can make an instance variable by adding double underscores before its name. For example,'''
# Python program to demonstrate private members of the parent class
# class C(object):
#     def __init__(self):
#         self.c = 21

#         # d is private instance variable
#         self.__d = 42

#     # def myfunc(self):
#     #     print(self.__d)

# class D(C):
#     def __init__(self):
#         self.e = 84
#         C.__init__(self)

# object1 = D()
# # obj = C()
# # produces an error as d is private instance variable
# print(object1.__d)

'''Since 'd' is made private by those underscores, it is not available to the child class 'D' and hence the error.'''

