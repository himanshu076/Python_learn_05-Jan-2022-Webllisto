'''List comprehension'''

# List comprehension is an elegent way to creats lists based on existing list.

list1 = [904,65,63,74,75,8,9,0,66,34,2,3,4,5,6,74,7,]
list1.sort()

list2 = [i for i in list1 if i > 10]
print(list2)