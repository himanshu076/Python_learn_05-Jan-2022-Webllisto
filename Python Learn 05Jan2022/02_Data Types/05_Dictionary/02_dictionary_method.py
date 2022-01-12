# print(dir(dict))

# dict = ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# print(len(dict))
# for i in dict:
#     print(i)


'''
__class__
__class_getitem__
__contains__
__delattr__
__delitem__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__gt__
__hash__
__init__
__init_subclass__
__ior__
__iter__
__le__
__len__
__lt__
__ne__
__new__
__or__
__reduce__
__reduce_ex__
__repr__
__reversed__
__ror__
__setattr__
__setitem__
__sizeof__
__str__
__subclasshook__
clear
copy
fromkeys
get
items
keys
pop
popitem
setdefault
update
values
'''

'''                 Methods Start here                '''

'''clear()'''
# car ={"brand": "Ford", "model": "Mustang", "year": "1964"}
# car.clear()
# print(car)

'''copy()'''
# car ={"brand": "Ford", "model": "Mustang", "year": "1964"}
# car.copy()
# print(car)

'''fromkeys()'''
# x = ('key1', 'key2', 'key3')
# y = 0
# thisdict = dict.fromkeys(x, y)
# print(thisdict)

# x = ('key1', 'key2', 'key3')
# thisdict = dict.fromkeys(x)
# print(thisdict)

'''get()'''
# car = {"brand": "Ford", "model": "mustang", "year":"1964"}
# x = car.get("year")
# print(x)

'''items()'''
# car = {"brand": "Ford", "model": "mustang", "year":"1964"}
# x = car.items()
# print(x)

'''keys()'''
# car = {"brand": "Ford", "model": "mustang", "year":"1964"}
# x = car.keys()
# print(x)

'''pop()'''
# car = {"brand": "Ford", "model": "mustang", "year":"1964"}
# car.pop("model")    # pop expected one arguments
# print(car)

'''popitem()'''
# car = {"brand": "Ford", "model": "mustang", "year":"1964"}
# car.popitem()
# print(car)

'''setdefaults()'''
# car = {"brand": "Ford", "model": "mustang", "year":"1964"}
# x = car.setdefault("model", "BMW")
# print(x)

# car = {"brand": "Ford", "model": "mustang", "year":"1964"}
# x = car.setdefault("color", "white")
# print(x)

'''update()'''
# car = {"brand": "Ford", "model": "mustang", "year":"1964"}
# car.update({"model": "BMW"})
# print(car)

'''values()'''
# car = {"brand": "Ford", "model": "mustang", "year":"1964"}
# x = car.values()
# print(x)