'''While loop'''
# count = 0
# while (count<3):
#     count = count + 1
#     print("Hello Himanshu")

# check list still contain any statement
# a = [1,3,2,4,5,7]
# while a:
#     print(a.pop())

# while in single line because single line statement
# count = 0
# while (count<5): count +=1; print("Hello Himanshu")

# *********************************************************************
'''Python while loop with continue statement'''
# Prints all letters except 'e' and 's'
# i = 0
# a = "greeksforgreeks"

# while i < len(a):
#     if a[i] == 'e' or a[i] == 's':
#         i += 1
#         continue
#     print('Current Letter :', a[i])
#     i += 1

'''Python while loop with break statement'''
# break the loop as soon it sees 'e' or 's'
# i = 0
# a = "greeksforgreeks"
# while i <= len(a):
#     if a[i] == 'e' or a[i] == 's':
#         i += 1
#         break
#     print('Current Letter: ', a[i])
#     i += 1


'''Python while loop with pass statement'''

# a = "greeksforgreeks"
# i = 0
# while i < len(a):
#     i += 1
#     pass

#     print('value of i :', i)

'''Python while loop with else'''

# while-else loop without break
# i = 0
# while i < 4:
#     i += 1
#     print(i)
# else: # Executed because no break in while
#     print("No Break\n")

# while-else loop with breakss
# i = 0
# while i < 4:
#     i += 1
#     print(i)
	# break
# else: # Not Executed as there is a break
	# print("No Break")

'''Sentinel Controlled Statement'''

# python while loop with user input
# a = int(input('Enter a number (-1 to quit)'))
# while a != -1:
#     a = int(input('Enter a number (-1 to quit)'))


'''while loop Practice question start here'''
'''Q1. Write a program to print the following using while loop'''
# First 10 even number
# i = 0
# while i < 20:
#     i += 2
#     print(i)

# First 10 odd number
# i = 1
# while i < 20:
#     print(i)
#     i += 2

# First 10 Natural number
# i = 0 
# while i < 10:
#     i += 1
#     print(i)

# First 10 Whole Number
# i = 0
# while i < 10:
#     print(i)
#     i += 1

'''Q2. Write a program to print first 10 integers and their squares using while loop.'''

# i = 0
# print("Numbers\tSquares")
# while i < 10:
#     i += 1
#     # print(i, i*i)
#     print(i,"\t", i**2)

'''Q3. Write for loop statement to print the following series:
10, 20, 30 … … 300'''
# i = 10
# while i <= 300:
#     print(i, end = " ")
#     i += 10

'''Q4. Write a while loop statement to print the following series
105, 98, 91 ………7.'''
# i = 105
# while i >= 7:
#     print(i, end = " ")hie
#     i -= 7
	
'''Q5. Write a program to print first 10 natural number in reverse order using while loop.'''
# i = 10
# while i > 0:
#     print(i) 
#     i -= 1


"""                 Programs of while loop in python                    """
'''Q6. Write a program to print sum of first 10 Natural numbers.'''
# n = 10
# i = 0
# while i < 10:
#     n = n + i
#     i += 1
# print (n)

'''Q7. Write a program to print sum of first 10 Even numbers.'''
# i = 0
# n = 0
# while i <= 20:
#     n = n + i
#     i += 2
# print(n)

'''Q8. Write a program to print table of a number entered from the user.'''
# num = int(input("Enter the number for table: \n"))
# i = 0
# while i <= 10:
#     s = num * i
#     # print(s)
#     print(num, "*", i, "=", s)
#     i += 1

'''Q9. Write a program to find the sum of all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.'''
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1>num2:
#     while num1 > num2:
#         if num2 % 2 == 0:
#             num2 += 1
#             print(num2)
# else:
#     while num2 > num1:
#         if num1 % 2 == 0:
#             num1 += 1
#             print(num1)
			
'''Q10. Write a program to check whether a number is prime or not using while loop.'''
# First Method
# num = int(input("Enter your number: "))
# while num:
	# import pdb; pdb.set_trace()
	# if num % 2 != 0:
	#     print(num, "is prime number")
	# else:
	#     print(num, "is not a prime number")
	# break

# Second Method:
# num1 = int(input("Enter any number : "))
# k=0
# if num1 == 0 or num1 == 1:
#     print("Not a prime number ")
# else:
#    i = 2
#    while(i<num1):
#      if num1 % i == 0:
#        k = k+1
#      i = i+1
# if k == 0 :
#         print( num1,"is prime number")
# else:
#         print(num1, "is not prime number")

'''Q11. Write a program to find the sum of the digits of a number accepted from the user.'''
# num = int(input("Enter your number: "))
# i=0
# k=0
# while num != 0:
#     # import pdb; pdb.set_trace()
#     i = num % 10
#     k = k + i
#     num = num//10
#     print(k)

'''Q12. Write a program to find the product of the digits of a number accepted from the user.'''
# num =  int(input("Enter your number: "))
# k = 1
# while num != 0:
#     # import pdb; pdb.set_trace()
#     i = num % 10
#     k = k * i
#     num = num//10
# print(k)

'''Q13. Write a program to reverse the number accepted from user using while loop.'''
# Method 1:
# num = int(input("Enter Your number: "))
# k = ""
# while num != 0:
#     i = num % 10
#     s = str(i)
#     k = k + s
#     num = num//10
# print(k) # giving output in str

# Method 2:
# num = int(input("Enter your number: "))
# k = 0
# while num != 0:
#     i = num % 10
#     k = k * 10 + i
#     num = num//10
# print(k)

'''Q14. Write a program to display the number names of the digits of a number entered by user, for example if the number is 231 then output should be Two Three One
'''
# num = input("Enter Your Number: ")
# l1 = list(num)
# l2 = len(l1)
# n = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
# i = 0
# while i < l2:
#     print(n[int(l1[i])], end=" ")
#     i = i + 1

'''Q15. Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop.'''

# num = int(input("Enter your num: "))
# a = 0; b = 1
# i = 0
# while i < num:
#     a, b = b, a+b
#     i = i + 1
#     print(a, end=" ")

'''Q16. Write a program to print the factorial of a number accepted from user.'''
# num = int(input('Enter your num: '))
# i = 1
# f = 1
# while i <= num:
#     f = f * i
#     i += 1
# print(f)

'''Q17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)'''
# num = int(input("enter your num: "))
# n = num
# l1 = str(num)
# i = 0
# r = 0
# while i < len(l1):
#     s = num % 10
#     y = s**3
#     r = r + y
#     i += 1
#     num = num//10
# s = r
# if s == n:
#     print(f"{n} is Armstrong number")
# else:
#     print(f"{n} not Amstrong number ")

'''Q18. Write a program to add n terms of the following series using a while loop:
1/1! + 1/2! + 1/3! + …….. + 1/n!'''
# num = int(input("Enter your num: "))
# i = 1
# f = 1
# sum = 0
# while i < num:
#     f = f * i
#     sum = sum + i/f
#     i += 1
#     print(round(sum, 2))

'''Q19. Write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered.'''
# Method 1:
# i = "+"
# num1 = 0
# while i == "+":
#     num = int(input("Enter your num: "))
#     num1 = num1 + num
#     i = input("more using '+' operator - Enter for Exit & sum")
# print(num1)

# Method 2 using "for" loop:
# p = int(input("Enter your numbers seperated by + sign:").split("+"))
# s = 0
# for r in p:
#     s = s + int(r)
# print(s)

'''Q20. Write a program to enter the numbers till the user enter ZERO and at the end it should display the count of positive and negative numbers entered.'''
# Method 1:
# add = 0
# i = 1
# while i:
#     num = int(input("Enter your num: "))
#     add = add + num
#     # print(add)
#     if num:
#         i += 1
#     if num == 0:
#         print(add)
#         break

# Method 2:
# num = 1
# posnum = 0
# negnum = 0
# while num != 0:
#     num = int(input())
#     if num > 0:
#         posnum = posnum + num
#     else:
#         negnum = negnum + num
# print(f"sum of all positive number: {posnum}")
# print(f"sum of all negtive number: {negnum}")

'''Q21. Write a program to find the HCF of two numbers entered from the user.'''

num1 = int(input("Enter your number 1: "))
num2 = int(input("Enter your number 2: "))
i = 1

if num1 > num2:
	while i !=0:
		import pdb; pdb.set_trace()
		i = num1 % num2
		if i == 0:
			hcf = num2
		else:
			num1 = num2
			num2 = i
else:
	while i !=0:
		import pdb; pdb.set_trace()
		i = num2 % num1
		if i == 0:
			hcf = num1
		else:
			num2 = num1
			num1 = i
print(hcf)

