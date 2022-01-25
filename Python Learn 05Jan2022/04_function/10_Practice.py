'''Python fuction - Exerciese, Practice'''

'''Q1. Write a Python function to find the Max of three numbers.'''
# method 1:
# def maxOfThree(x, y, z):
#     if x>y and x>z:
#         print(x)
#     elif y>x and y>z:
#         print(y)
#     else:
#         print(z)

# maxOfThree(40, -30, 55)
    
# method 2:
# def maxNum(*args):
#     x = []
#     for arg in args:
#         x.append(arg)
#         # print(x)
#     z = max(x)
#     return type(z)

# y = maxNum(10,30,40,50)
# print(y)
        
'''Q2. Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)'''
# Method 1:
# def sumOfNum(*args):
#     l = list(args)
#     s = 0
#     for sum in l:
#         s = s + sum
#     return s

# y = sumOfNum(10, 20, 30, 40, 50)
# print(y)

# Method 2:
# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))

'''Q3. Write a Python function to multiply all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, -1, 7)'''

# def multiplyOfNum(*args):
#     s = list(args)
#     k = 1
#     for mtply in s:
#         k *= mtply
#     return k
# y = multiplyOfNum(2, 3, 5, 4)
# print(y)

'''4. Write a Python program to reverse a string. Go to the editor
Sample String : "1234abcd"
xpected Output : "dcba4321"'''
# Method 1:
# def reverseStr(args):
#     return args[::-1]

# y = reverseStr("1234abcd")
# print(y)

# Method 2:
# def reverseStr(vin):
#     rst = ''
#     indx = len(vin)
#     while indx>0:
#         rst += vin[indx-1]
#         indx = indx-1
#     return rst

# y = reverseStr("1234abcd")
# print(y)

'''Q5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.'''
# Method 1:
# def calFact(fctrl):
#     f = 1
#     i = 1
#     while i <= fctrl:
#         f *= i
#         i += 1
#     return f

# y = calFact(5)
# print(y)

# Method 2:
# def calFact(fctrl):
#     if fctrl == 1 or fctrl == 0:
#         return 1
#     else:
#         return fctrl*calFact(fctrl-1)
# y = calFact(4)
# print(y)
        
'''Q6. Write a Python function to check whether a number falls in a given range.'''
# Method 1:
# def NumInRange(num):
#     if num in range(5, 12) or num in range(18, 26):
#         print(f"{num} is in list")
#     else:
#         print(f"{num} not in list")

# NumInRange(25)

# Method 2:
# def NumInLst(n, start_num, end_num=0):
#     return start_num <= n <= end_num if end_num >= start_num else end_num <= n <= start_num

# print(NumInLst(30, 10, 30))

'''Q7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''
# Method 1:
# def countUpperLowerChar(str1):
#     upper = 0
#     lower = 0
#     for i in str1:
#         if i.isupper():
#             upper += 1
#         elif i == " ":
#             ""
#         else:
#             lower += 1
#     return f"Number of upper character is {upper} & Number of lower caracter is {lower}"

#     # s = str1.upper()
#     # print(s)
# y = countUpperLowerChar("The quick Brow Fox")
# print(y)

# Method 2:
# def countUpperLowerChar(str3):
#     str1 = str3.replace(" ", "")
#     upper = 0
#     lower = 0
#     str2 = str1.upper()
#     for i in range(len(str1)):
#         if str1[i] == str2[i]:
#             upper += 1
#         else:
#             lower += 1
#     return f"Number of upper character is {upper} & Number of lower caracter is {lower}"

# y = countUpperLowerChar("The quick Brow Fox")
# print(y)

'''Q8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''
# method 1:
# def uniqueList(list1):
#     set2 = set(list1)
#     list3 = list(set2)
#     return list3

# y = uniqueList([1,2,3,3,3,3,4,5])
# print(y)

# Method 2:
# def unique_list(lst):
#     x = []
#     for i in lst:
#         if i not in x:
#             x.append(i)
#     return x

# y = unique_list([1,2,3,3,3,3,4,5])
# print(y)

'''Q9. Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.'''

# def primeNumber(num):

#     if num == 1:
#         return (f"{num} is prime number.")
#     elif num == 2:
#         return (f"{num} is prime number.")
#     else:
#         for x in range(2,num):
#             if num % x == 0:
#                 return (f"{num} is not prime number.")
#         return (f"{num} is prime number.") 

# y = primeNumber(112)
# print(y)

