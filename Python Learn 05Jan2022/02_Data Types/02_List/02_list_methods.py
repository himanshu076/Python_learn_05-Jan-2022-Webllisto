'''
Method	        Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

'''clear'''
# fruits = ['apple', 'banana', 'cherry', 'orange']
# x = fruits.clear()

'''copy'''
# fruits = ['apple', 'banana', 'cherry', 'orange']
# x = fruits.copy()

'''count'''
# fruits = ['apple', 'banana', 'cherry']
# x = fruits.count("cherry")

'''extend'''
# fruits = ['apple', 'banana', 'cherry']
# cars = ['Ford', 'BMW', 'Volvo']
# fruits.extend(cars)

'''index''' # showing position
# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry")
# print(x)

'''insert'''
# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(1, "orange")
# print(fruits)

'''pop()'''
# fruits = ['apple', 'banana', 'cherry']
# fruits.pop(1)

'''remove'''
# fruits = ['apple', 'banana', 'cherry']
# fruits.remove("banana")
# print(fruits)

'''reverse'''
# fruits = ['apple', 'banana', 'cherry']
# fruits.reverse()
# print(fruits)

'''sort'''
# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort()
# print(cars)

# print(dir(list))

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']