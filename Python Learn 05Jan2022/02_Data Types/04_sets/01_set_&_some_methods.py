'''Sets Definitions'''
'''
What is a Python set? A set is an unordered and mutable collection of unique elements. Sets are written with curly brackets ({}), being the elements separated by commas. The following code block shows two sets, containing a collection of numbers and cities
'''
'''
A set is a mutable unordered collection with no duplicate elements.
'''

'''Creating a Set'''

# Creating a Set with the use of a String
# set1 = set("GeeksForGeeks")
# print("\nSet with the use of String: ")
# print(set1)
 
# Creating a Set with
# the use of Constructor
# (Using object to Store String)
# String = 'GeeksForGeeks'
# set1 = set(String)
# print("\nSet with the use of an Object: " )
# print(set1)
 
# Creating a Set with
# the use of a List
# set1 = set(["Geeks", "For", "Geeks"])
# print("\nSet with the use of List: ")
# print(set1)

'''Adding Elements to a Set'''

'''Using Add() Method'''

# Creating a set
# set1 = set()
# print(set1)

# Adding element and tuple to the Set
# set1.add(8)
# set1.add(9)
# set1.add((6,7))
# print(set1)

# Adding elements to the Set using Iterator
# for i in range(1,6):
#     set1.add(i)
# print(set1)

'''Using update() method'''
# Addition of elements to the Set using Update function
# set1 = set([4, 5, (6, 7)])
# set1.update([10, 11])
# print(set1)

'''Accessing a Set'''

# set1 = set(["Geeks", "For", "Geeks"])
# print(set1)
 
# Accessing element using
# for loop
# print("\nElements of set: ")
# for i in set1:
#     print(i, end=" ")
 
# Checking the element
# using in keyword
# print("Geeks" in set1)

# ********************************************************************************************

'''Removing elements from the Set'''

'''Using remove() method or discard() method'''

# set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(set1)

# set1.remove(5)
# set1.remove(6)
# print(set1)                                                                                               

# set1.discard(5)
# set1.discard(6)
# print(set1)

# for i in range(1, 5):
#     set1.remove(i)
# print(set1)

'''Using pop() method'''
# set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# set1.pop()
# print(set1)

'''Using clear() method'''
# set1 = set([1, 2, 3, 4, 5])
# set1.clear()
# print(set1)