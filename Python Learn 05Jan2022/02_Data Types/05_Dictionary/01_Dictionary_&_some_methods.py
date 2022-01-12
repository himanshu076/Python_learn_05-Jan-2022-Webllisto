'''Dictionary Defination'''
'''
Dictionary in Python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.
'''
'''Dictionary — A dictionary is a mutable unordered collection that Python indexes with name and value pairs.'''
'''Note - Keys in a dictionary don't allow Polymorphism.'''

'''Creating Dictionary'''
# Creating a Dictionary with integer keys
# Dict = {1:"shubham", 2:"deepesh", 3:"kishor", 4:"rakesh", 5:"meena"}
# Dict = {'name1':"shubham", 'name2':"deepesh", 'name3':"kishor", 'name4':"rakesh", 'name5':"meena"}
# print(Dict)
# print(Dict[1])
# print(Dict['name3'])

# Creating a Dictionary with mixed keys
# Dict = {'name':"kishor", 2:[1, 2, 3, 4, 5]}
# print(Dict)

# Creating an empty dictionary
# dict = {}
# print(dict)

# creating a dictionary with dict() method
# dict = dict({1:"shubham", 2:"kishor", 3:"dinesh"})
# print(dict)

# creating a dictionary with each item as a pair
# dict = dict([(1, "kishor"), (2, "sheela")])
# print(dict)

'''Nested Dictionary'''
# Creating a Nested dictionary
# dict = {1:"mango", 2:"orange", 3:{"A":"welcome", "B":"to", "c":"new office"}}
# print(dict)

'''Adding elements to dictionary'''
dict = {}
# Adding an element one at a time

dict[0] = 'dilip'
dict[1] = 'guru'
dict[2] = 'pinky'
# print(dict)

# Adding set of vale to a single key
# dict['value_set'] = 2, 3, 4
# print(dict)
# print(type(dict['value_set']))

# updating existing key's value
# dict[2] = 'Welcome'
# print(dict)

# Ading nested key value to dictionary
# dict[5] = {'Nested' : {'1': 'Life', '2':'Aman'}}
# print(dict)

'''Accessing elements from a Dictionary'''
# accessing a element using key
# dict = {1:"vegi", 'name':'vinay', 2:'nonveg'}
# print(dict['name'])
# print(dict[1])

# Accessing a element using a get() method
# print(dict.get(2))

'''Accessing an element of a nested dictionary'''
# dict = {'dict1':{1:'greeks'}, 'dict2':{'name':'for'}}
# print(dict)
# print(dict['dict1'])
# print(dict['dict1'][1])
# print(dict['dict2']['name'])

'''Removing Elements from Dictionary'''
'''using Del keyword'''
# Initial Dictionary
# dict = {5:'welcome', 6:'To', 7:'office', 'A':{1:'dingi', 2:'dinga', 3:'ding'}, 'b':{1:'kishor', 2:'Life'}}
# print(dict)

# del dict[6]
# del dict['A'][2]
# del dict
# print(dict)

'''Using pop() method'''
# dict = {1:"kishor", 'name':"shivam", 3:"shivangi"}
# pop_ele = dict.pop(1)
# print(dict)
# print(pop_ele) # printing pop method deleted value 

'''using popitem() method   '''
# dict = {1:"kishor", 'name':"shivam", 3:"shivangi"}
# pop_ele = dict.popitem()
# print(str(dict))
# print(type(pop_ele))
# print(pop_ele)

'''Using clear() method'''
# All the items from a dictionary can be deleted at once by using clear() method.
# dict = {1:"shubham", 'name':"deepmala", 3:"vinay"}
# dict.clear()
# print(dict)

