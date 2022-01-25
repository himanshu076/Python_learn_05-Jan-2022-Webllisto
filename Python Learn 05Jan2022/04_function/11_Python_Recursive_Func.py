'''****************Python Recursive Function******************'''

'''Q1. Write a Python program to calculate the sum of a list of numbers.'''

# def in(a):
#     if len(a) == 1:
#         return a[0]
#     else:
#         return a[0] + calculate_Sum(a[1:])

# s = calculate_Sum([30, 20, 40, 50])


def calculate_sum(*a):
    m = a.split("+")
    s = a + calculate_sum(a)
    return s

z = calculate_sum(y)
print(z)

