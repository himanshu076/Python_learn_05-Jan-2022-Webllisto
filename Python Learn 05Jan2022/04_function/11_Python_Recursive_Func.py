'''****************Python Recursive Function******************'''

'''Q1. Write a Python program to calculate the sum of a list of numbers.'''

# def in(a):
#     if len(a) == 1:
#         return a[0]
#     else:
#         return a[0] + calculate_Sum(a[1:])

# s = calculate_Sum([30, 20, 40, 50])


'''Q2. Write a Python program to converting an Integer to a string in any base. '''
# def int_base(n, base):
#     if base > 0:
#         s = f"{n}" + "0"*base
#     else:
#         return n
#     return s

# y = int_base(50, 3)
# print(y)

# right answer

# def to_string(n,base):
#    conver_tString = "0123456789ABCDEF"
#    if n < base:
#       return conver_tString[n]
#    else:
#       return to_string(n//base,base) + conver_tString[n % base]
# print(to_string(4567,16))

'''Q3. Write a Python program of recursion list sum. Go to the editor
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21'''
# def list_sum(lst):
#     total = 0
#     for ele in lst:
#         if type(ele) == type([]):
#             total = total + list_sum(ele)
#         else:
#             total = total + ele

#     return total

# k = list_sum([1,2, [3,4], [5,6]])
# print(k)

'''Q4. Write a Python program to get the factorial of a non-negative integer.'''

# def fact_of_num(n):
#         if n <= 1:
#             return 1
#         else:
#             n = n * fact_of_num(n-1)
#         return n

# y = fact_of_num(6)
# print(y)

'''Q5. Write a Python program to solve the Fibonacci sequence using recursion.'''
# simple function
# def fib_series(n):
#     a = 0; b = 1
#     for i in range(n):
#         a, b = b, b+a
#     return a
# y = fib_series(10)
# print(y)

# recurcive function
# def fib_series(n):
#     if n ==1 or n == 2:
#         return 1
#     else:
#         return fib_series(n-1) + fib_series(n-2)

# y = fib_series(8)
# print(y)

# from datetime import datetime


# def add(n):
#     print("adding 5")
#     time = datetime.now()
#     print(time)
#     return n+5

# def adding(n):
#     print("adding 10")
#     time = datetime.now()
#     print(time)
#     return n+10

# def summation():
#     print("under summation")
#     return add(8)+adding(8)

# print(summation())

'''6. Write a Python program to get the sum of a non-negative integer. Go to the editor
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9'''

# def sum_Digits(digit):
#     k = 0
#     if digit != 0:
#         s = (int(digit) % 10)
#         k = s + sum_Digits(digit // 10)
#         digit = digit//10

#     return k
    
# y = sum_Digits(50988)
# print(y)

# SOLVED METHOD

# def sum_Digits(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + sum_Digits(n//10)
    
# y = sum_Digits(-54)
# print(y)

'''Q7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). Go to the editor
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30'''

# def n_Series(n):
#     if n < 1:
#         return 0
#     else:
#         return n + n_Series(n-2)

# y = n_Series(10)
# print(y)

'''Q8. Write a Python program to calculate the harmonic sum of n-1. Go to the editor
Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example :
harmonic series'''

# def harmonic_Sum(n):
#     if n < 2 :
#         return 1
#     elif n <= 0:
#         return 0
#     else:
#         return 1/n + harmonic_Sum(n-1)

# y = harmonic_Sum(7)
# print(y)

'''Q9. Write a Python program to calculate the geometric sum of n-1. Go to the editor
Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.
Example : a = 1 and r = 1/2, or
geometric series - a + ar + ar2 + ar3+⋯, ***---- 1 + 1/2 + 1/4 + 1/8 +⋯,'''

# def geometric_series(n):
#     if n < 0:
#         return 0
#     else:
#         return 1/(2 ** n) + geometric_series(n-1)

# y = geometric_series(7)
# print(y)

'''Q10. Write a Python program to calculate the value of 'a' to the power 'b'. Go to the editor
Test Data :
(power(3,4) -> 81'''

# def power_Of_Num(a, n):
#     if n == 0:
#         return 1
#     elif a == 0:
#         return 0
#     else:
#         return a*power_Of_Num(a, n-1)

# y = power_Of_Num(5, 3)
# print(y)

'''Q11. Write a Python program to find  the greatest common divisor (gcd) of two integers. '''
# def recursiveGcd_HCF(a, b):
#     low = min(a, b)
#     high = max(a, b)

#     if  low == 0:
#         return high
#     elif low == 1:
#         return 1
#     else:
#         return recursiveGcd_HCF(low, high%low)

# y = recursiveGcd_HCF(10, 24)
# print(y)
