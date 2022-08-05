'''Python map() function
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax : map(fun, iter)

Parameters : fun : It is a function to which map passes each element of given iterable.
             iter : It is a iterable which is to be mapped.

NOTE : You can pass one or more iterable to the map() function.

Returns : Returns a list of the results after applying the given function  
          to each item of a given iterable (list, tuple etc.) 
 
NOTE :  The returned value from map() (map object) then can be passed to functions like list()(to create a list), set() (to create a set) .'''

'''Example 1: '''
# def addition(n):
#     return n + n

# # we double all number usning map function
# numbers = (3, 4, 5, 7, 8)
# result = map(addition, numbers)
# print(list(result))


# Example 2:
# numbers = (3, 4, 6, 7, 8, 9, 2)
# result = map(lambda x: x + x, numbers)
# print(list(result))

# Example 3:
# numbers1 = (3, 4, 6, 7, 8, 9, 2)
# numbers2 = reversed((3, 4, 6, 7, 8, 9, 2))
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))

# Example 4:
# l = ['deepak', 'kishor', 'sumit', 'sonam', ]
# test = list(map(list, l))
# print(test)
