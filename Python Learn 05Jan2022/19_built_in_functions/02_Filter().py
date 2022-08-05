'''filter() in python
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

syntax:

filter(function, sequence)
Parameters:
function: function that tests if each element of a 
sequence true or not.
sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.
Returns:
returns an iterator that is already filtered.'''

'''example 1:'''

# def func(variable):
#     letters = ["a", "e", "o", "i", "u"]

#     return False if variable in letters else True

# sequence2 = ["k", "d", "r", "e", "w", "y", "i"]
# filtered = filter(func, sequence2)

# for s in filtered:
#     print(s, end=" ")

'''******************Application******************'''
'''It is normally used with Lambda functions to separate list, tuple, or sets.'''

# seq = [4,5,6,7,8,3,2]
# result3 = filter(lambda x: x % 2 !=0, seq)
# print(list(result3))

# result3 = filter(lambda x: x % 2 ==0, seq)
# print(list(result3))


'''Python filter() Function Example 3'''

# Python filter() function example  
def mulof3(val):  
    if val%3==0:  
        return val      
# Calling function  
result = filter(mulof3,(1,3,5,6,8,9,12,14))  
# Displaying result  
result = list(result)  
print(result) # multiples of 3

