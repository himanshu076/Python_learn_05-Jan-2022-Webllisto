'''String Logical Questions'''

'''Question 1: Write a code to store following string in a variable named 'str'    This is amit's block '''
'''Solutions'''
# str = "This is amits's block"
# str = "This is amits\'s block"
# print(str)

'''Question 2: write the output of the following code'''
# str1 = "welcome to my blog"
# str2 = "welcome to my \n blog"
# print(str1)
# print(str2)

'''Question 3: Write the output of the following code'''
# a. 
# str = "hello"
# print(str[:3])

# g.
# for i in range(2,7,2):
#     print(i * '2')

# h.
# for i in range(3,12,2):
#     print("a".upper())

# i.
# for i in range(3,12,2):
#     print("a".upper)

# j.
# s = "welcone to my site https and good website"
# print(s.find('o', 10, 20))

'''Question 4: write a code to create empty string 'str1'? '''
# str1 = ""

'''Question 5: write a code to assing a string "hello world"' to a string variable name str1'''
# str1 = "Hello World"

'''Question 6: write a program to display each character of the following string in seperate line using "for Loop" 
str1 = "Welcome to my blog"
'''
# str1 = "Welcome to my blog"
# for i in str1:
#     print(i)

'''Question 7: write a program to display each character of the following string in seperate line using "for Loop
str1 = "Welcome to my blog"
'''
# str1 = "Welcome to my blog"
# i = 0
# while i<len(str1):
#     print(str1[i])
#     i += 1
# print()

'''Question 8: Write a program to count the length of string without using inbuilt function.'''
# str1 = "this is table where my laptop is keep on it and right now i'm using it."
# i = 0
# for b in str1:
#     i += 1
# print(i)

'''Question 9: Writwe the code to join string 'str1' and 'str2' and store the result in variable 'str3' '''
# var1 = 'Welcome to '
# var2 = 'the new world!'
# var3 = var1 + var2
# print(var3)

'''Question 10: Writw the output of the following'''
# for i in "Amit":
#     print(i in "Amit")

'''Question 11: statement - True or False'''
# print("Amit" > "amitabh")

'''Question 12: Write a program to accept string and display total number of alphabets.'''
# str1 = input("Enter Your String: \n")
# c=0
# for i in str1:
#     if i.isalpha()==True:
#         c += 1
# print(c)

'''Question 13: Write a program to accept string and display the sum of digits, if any present in string'''
# str1 = input("Enter your string: \n")
# c=0
# for i in str1:
#     # if i.isnumeric()==True:
#     if i.isdigit()==True:
#         c += 1
# print(c)

'''Question 14: Write a program to acept a string and convert it into lowercase'''
# str1 = input("Enter your string: \n")
# print(str1.lower())

'''Question 15: Write a program to count the number of lowercase and uppercase in a string accepted from the user'''
# str1 = input("Enter your string: \n")
# c=0; b=0
# for i in str1:
#     if i.islower()==True:
#         c += 1
#     if i.isupper()==True:
#         b += 1
# print(f"Number of lower character is {c} & Upper character is {b}")

'''Question 16: write a program to accept a string and display each word and it's length.'''
# Method 1:
# str1 = input("Enter your string: \n")
# x = str1.split()
# for i in x:
#     print(i, len(i))

# Method 2:
# c=0
# for i in str1:
# #     print()
#     print(i, c)   
#     c=c+1

'''Question 17: Write a program to accept a string and display string with capital letter of each word.'''
# Method 1:
# str1 = input("Enter your string: \n")
# print(str1.title())

# Method 2: 
# x = str1.split()
# str2 = ""
# for i in x:
#     str2 = str2 + " " + i.capitalize()
# print(str2)

'''Question 18: Write a program to replace all the word 'do' with 'done' in the following string'''
# Method :
# str1 = "I do you do and we all will do"
# x = str1.replace('do', 'done')
# print(x)

# Methos 2:
# str = str1.split()
# for c in str:
#     if c == "do":
#         c = "done"
#     print(c, end=" ")
# print(type(c))

'''Question 19: Accept a string and display in reverse order'''
# str1 = "this is OS means Operating System"
# print(str1[::-1])

'''Question 20: '''
# method 1:
# str1 = "this is OS means Operating System"
# a=1
# while a<=20:
#     print(str1, a)
#     a += 1

# Method 2:
# str1 = input("Enter your string: \n")
# for i in range(20):
#     print(str1, i)

'''Question 21: Write a program to accept a string in python and display the entire string in upper case'''
# str1 = input("Enter your string: \n")
# print(str1.upper())

'''Question 22: Write a program to accept a string and display last three characters of the string'''
# str1 = input("Enter your string: \n")
# for a in str1:
#     x = str1[-3:]
# print(x)

'''Question 23: Write a program to accept a string and display the entire string in lower case'''
# str1 = input("Enter your string: \n")
# print(str1.lower())

'''Question 24: Accept a string and display the entire string with first and last character in upper case'''
# str1 = input("Enter your string: \n")
# print(str1[0].upper() + str1[1:-1] + str1[-1].upper())

'''Question 25: Write a program to accept a string and display first three character of string'''
# str1 = input("Enter your string: \n")
# print(str1[0:3])

'''Question 26: Write a function in python which accept a string as argument and display total number of vowels'''
# Method 1:
# def vowelFun():
#     str1 = input("Enter your string: \n")

#     x = str1.count("a")
#     y = str1.count("e")
#     z = str1.count("o")
#     c = str1.count("i")
#     a = str1.count("u")
#     print(x+y+z+c+a)
# vowelFun()    # calling a function

# Method 2:
# str1 = input("Enter your string: \n")
# def vowCount(str1):
#     v=0
#     for i in range(len(str1)):
#         if str1[i] in "aeoiuAEOIU":
#             v += 1
#     print("Total number of Vowels are ", v)
# vowCount(str1)

'''Question 27: Write a function in python which accept a string as argument and display total number of lower case characters'''
# Method 1:
# str1 = input("Enter your string: \n")
# def lowerCount(str1):
#     v=0
#     for i in range(len(str1)):
#         if str1[i].islower():
#             v += 1
#     print(v)
# lowerCount(str1)

# Method 2:
# def lowerCount(str1):
#     v=0
#     a="abcdefghijklmnopqrstuvwxyz"
#     for i in range(len(str1)):
#         if str1[i] in a:
#             v += 1
#     print(v)

# lowerCount(str1)

'''Question 27: Write a function in python which accept a string as argument and display total number of digits'''
# Method 1:
str1 = input("Enter your string: \n")
# def totalDigit(str1):
#     v = 0
#     for i in range(len(str1)):
#         if str1[i].isdigit():
#             v += 1
#     print(v)
# totalDigit(str1)

# Method 2:
# def totalDigit(str1):
#     v = 0
#     a = "0123456789"
#     for i in range(len(str1)):
#         if str1[i] in a:
#             v += 1
#     print(v)
# totalDigit(str1)
