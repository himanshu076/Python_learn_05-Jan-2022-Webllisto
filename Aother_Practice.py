'''multiple input from user with + sign seperator & take the sum'''
# n = int(input("Enter num how many num you want to add"))
# s = 0
# for i in range(n):
#     # i = int(input("Enter your numbers seperated by + sign: "))
#     # i = int(input("type num & enter continue until you type initial num for add: "))
#     s = s + i 
# print(s)
# s = 0
# i = 0
# while i=="enter":
#     a = int(input("enter num: "))
#     s = s + a
#     i += 1
# print(s)

# Method 2 using "for" loop:
# p = int(input("Enter your numbers seperated by + sign:").split("+"))
# s = 0
#     for r in p:
#         s = s + int(r)
#     print(s)

# Update code
p = int(input("Enter your numbers seperated by + sign:").split("+"))
if p == str:
    print("Enter a valid number :")
else:
    s = 0
    for r in p:
        s = s + int(r)
    print(s)