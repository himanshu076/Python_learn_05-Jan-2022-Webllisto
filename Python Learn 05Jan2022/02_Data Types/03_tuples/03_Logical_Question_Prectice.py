'''Q1. Write a Python program to create a tuple.'''
# t1 = (2,3,4,5,5,6,7,8,9)
# print(t1)
# print(type(t1))

'''Q2. Write a Python program to create a tuple with different data types'''
# t1 = ("kishor4322", [1,2,3,4], {2,3,4,'ds'}, {"name":"kishor"}, 3.0, 10, True, (1,2,3,4,5) )
# complex data is not storing
# print(t1)

'''Q3. Write a Python program to unpack a tuple in several variables.'''

# tuplex32 = 3,4,5
# print(type(tuplex32))

# t1, t2, t3 = tuplex32
# print(type(tuplex32))

'''Q4. Write a Python program to create a tuple with numbers and print one item.'''
# t1 = (2,3,4,5,6)
# print(t1[3])

'''Q5. Write a Python program to add an item in a tuple.'''
# t1 = 5,5,6,78,67
# t2 = 6,76,53,67,8,9
# a = list(t1)
# a.append(98)
# t2 = tuple(a)
# # print(t2)
# # print(t1+t2)

# tuplex = t1[1:3] + (45, 55, 67) + t2[2:4]
# print(tuplex)

'''Q6. Write a Python program to convert a tuple to a string.'''
# t1 = 4,5,6,78
# t2 = "a","d","d","f","g","h"
# s1 = str(t1)
# print(s1)
# # print(type(t2))
# s2 = "".join(t2)
# print(s2)

'''Q7. Write a Python program to get the 4th element and 4th element from last of a tuple.'''
# t1 = "t", "y", "u", "i", "o" "p", "r", "j"
# print(type(t1))

'''Q8. Write a Python program to create the colon of a tuple.'''
# from copy import deepcopy
# tuplex = ("HELLO", 5, [], True)
# print (tuplex)
# tuplex2 = deepcopy(tuplex)

# tuplex2[2].append(77)
# print(tuplex2)
# print(tuplex)

'''Q9. Write a Python program to find the repeated items of a tuple.'''
# tup = 6, 6, 7, 8, 8, 9, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0
# print(type(tup))
# print(tup)

# Removing copy from tuple
# tup1 = set(tup)
# print(type(tup1))
# print(tup1)
# tup2 = tuple(tup1)
# print(tup2)

# **************************************************************************

# program that count repeated tuple
# tup = (6, 6, 7, 8, 8, 9, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0)
# tup1 = list(tup)
# print(tup1)

# for i in range(len(tup1)):
# finalTup = []
# temp = []

# for j in tup1:
#     if j not in finalTup:
#         finalTup.append(j)
#     else:
#         temp.append(j)
# print(tuple(finalTup))

# **************************************************************************
# count repeated number from tuples
# tup = (6, 6, 7, 8, 8, 9, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0)
# print(tup.count(7))

'''Q10. Write a Python program to check whether an element exists within a tuple.'''

# tup = (6, 6, 7, 8, 8, 9, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0)
# try:
#     num = int(input())
#     if num in tup:
#         print(f"Yes {num} found in tup")
#     else:
#         print(f"{num} not found in tup")
    
# except ValueError:
#         print("Please enter a valid number")
        

'''Q11. Write a Python program to convert a list to a tuple.'''
# tup = [6, 6, 7, 8, 8, 9, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]
# print(list(tup))

'''Q12. Write a Python program to remove an item from a tuple.'''
# first Method
# tup = (6, 6, 7, 8, 8, 9, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0)
# tup1 = list(tup)
# tup1.remove(6)
# tup1.remove(6)
# tup1.remove(6)
# print(tup1)

# Second Method
# tup2 = tup1[0:4] + tup1[5:]
# print(tup2)

# Third Method
# tup1.remove(4)
# print(tup1)

'''Q13. Write a Python program to slice a tuple.'''
# tup = (6, 6, 7, 8, 8, 9, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0)
# print(tup[5:9])

# tup = ("Hello World")
# print(tup.index("d"))

'''Q14. Write a Python program to find the index of an item of a tuple.'''
# tup = (6, 6, 7, 8, 8, 9, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0)
# print(tup.index(8))

'''Q15. Write a Python program to find the length of a tuple.'''
# tup = (6, 6, 7, 8, 8, 9, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0)
# Method 1:
# for i in range(len(tup)):
#     pass
# print(i+1)    

# Method 2:
# tup1 = list(tup)
# tup2 = tup1.index(tup1[-1])
# print(tup2+2)

# Method 2:
# tup1 = len(list(tup))
# print(tup1)

