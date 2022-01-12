'''Python has a set of built-in methods that you can use on sets.'''
'''
Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two or more sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with another set, or any other iterable

'''

'''Add() method'''
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)

'''clear()'''
# fruits = {"apple", "banana", "cherry"}
# fruits.clear()
# print(fruits)

'''copy()'''
# fruits = {"apple", "banana", "cherry"}
# x = fruits.copy()
# print(x)

'''difference()'''
# x = {"apple", "banana", "cherry"}
# y = {"google", "apple", "microsoft"}

# z = x.difference(y)
# print(z)
# z = y.difference(x)
# print(z)

'''difference_update()'''
# x = {"apple", "banana", "cherry"}
# y = {"google", "apple", "microsoft"}

# x.difference_update(y)
# print(x)

'''discard()'''
# fruits = {"apple", "mango", "shubham", "kishor"}
# fruits.discard('mango')
# print(fruits)

'''intersection()'''
# x = {"apple", "mango", "orange"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)

# x = {"a", "b", "c"}
# y = {"c", "d", "e"}
# z = {"f", "g", "c"}
# results = x.intersection(y, z)
# print(results)

'''intersection_update()'''
# x = {"apple", "mango", "orange"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

# x = {"a", "b", "c"}
# y = {"c", "d", "e"}
# z = {"f", "g", "c"}
# x.intersection_update(y, z)
# print(x)

'''isdisjoint()'''
# x = {"apple", "mango", "orange"}
# y = {"google", "microsoft", "apple"}
# y = {"google", "microsoft", "facebook"}
# z = x.isdisjoint(y)
# z = y.isdisjoint(x)
# print(z)

'''issubset'''
# x = {"a", "b", "c"}
# x = {"a", "b", "l"}
# y = {"a", "b", "c", "d", "e", "f", "g"}
# z = x.issubset(y)
# print(z)

'''issuperset()'''
# x = {"a", "b", "c", "d", "e", "f", "g"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)

# x = {"a", "b", "k", "d", "e", "f", "g"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)

'''pop()'''
# x = {"a", "b", "k", "d", "e", "f", "g"}
# x.pop()
# print(x)

'''remove()'''
# x = {"a", "b", "k", "d", "e", "f", "g"}
# x.remove("d")
# x.remove("k")
# x.remove("f")
# print(x)

'''symmetric_difference()'''
# x = {"apple", "mango", "orange"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)

'''symmetric_difference_update()'''
# x = {"apple", "mango", "orange"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

'''union()'''
# x = {"apple", "mango", "orange"}
# y = {"google", "microsoft", "apple"}
# z = x.union(y)
# print(z)

# x = {"a", "b", "c"}
# y = {"f", "d", "a"}
# z = {"c", "d", "e"}
# result = x.union(y, z)
# print(result)

'''update()'''
# x = {"apple", "mango", "orange"}
# y = {"google", "microsoft", "apple"}
# x.update(y)
# print(x)