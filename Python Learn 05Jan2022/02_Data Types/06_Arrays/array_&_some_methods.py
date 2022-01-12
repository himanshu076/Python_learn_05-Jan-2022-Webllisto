'''Array Definitions'''
'''Python arrays are a data structure like lists. They contain a number of objects that can be of different data types. ... For example, if you have a list of student names that you want to store, you may want to store them in an array. Arrays are useful if you want to work with many values of the same Python data type.'''

'''Array in Python can be created by importing array module. array(data_type, value_list) is used to create an array with data type and value list specified in its arguments.'''

'''Creating a Array'''

# importing "array" for array creations
import array as arr

# creating array with integer type
# a = arr.array("i", [1, 2, 3])
# print(type(a))

# print ("The new created array is : ", end =" ")
# for i in range(0,3):
#     print(a[i], end=" ")
# print()

# creating an array with float type
# b = arr.array('d', [2.5, 5.5, 7.8])
# print ("The new created array is : ", end =" ")
# for i in range(0,3):
#     print(b[i], end=" ")

'''Adding elements to a array'''
# a = arr.array('i', [1,2,3])                   # i is for intiger
# for i in range(0, 3):
#     print(a[i], end=" ")

# inserting array using insert() function
# a.insert(1,4)
# for i in a:
#     print(i, end=" ")

# b = arr.array('d', [4.5, 2.5, 1.9])             # d is for float
# for i in range(0,3):
#     print(b[i], end=" ")

# adding an element using append()
# b.append(4.4)
# for i in b:
#     print(i, end=" ")
# print()

'''Accessing elements from the array'''
# a = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
# print(a[0])
# print(a[1])

# b = arr.array('d', [3.5, 8.5, 9.6, 7.2])
# print(b[0])
# print(b[3])
# print(b[2])

'''Removing Elements from the Array'''
# ary = arr.array('i', [1, 2, 3, 1, 5, 4, 8])
# for i in range(0, 7):
    # print(ary[i], end=" ")

# print(ary.pop(2))

# for i in range(0, 4):
#     print(ary[i])
# print('\r')

# ary.remove(1)           # remove is nonprintable
# for i in range(0, 3):
#     print(i, end=" ")

'''Slicing of array'''

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a = arr.array('i', l)         # converting list into array
# for i in a:
#     print(i, end=" ")

# range using slice Operation
# sliced_array = a[:5]
# print(sliced_array)

# sliced_array = a[2:]
# print(sliced_array)s

# sliced_array = a[:]
# print(sliced_array)

'''Searching element in array'''
# ary = arr.array('i', [1, 2, 3, 4, 3, 2, 1, 5])

# for i in range(0, 8):
#     print(ary[i], end=" ")

# print(ary.index(1))                 # Showing the occurrence/ index of the elements
# print(ary.index(4))                 # Showing the occurrence/ index of the elements

'''Updating elements in array'''
# ary = arr.array('i', [1, 2, 3, 4, 3, 2, 1, 5])

# for i in range(0, 6):
#     print(ary[i], end=" ")

# ary[2] = 6
# ary[4] = 9

# for i in range(0, 8):
#     print(ary[i], end=" ")
# print()

