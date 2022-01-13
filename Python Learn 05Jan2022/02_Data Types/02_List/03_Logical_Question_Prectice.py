
'''Question 1: Write a code to convert the string "Practice" into list.'''
# list = list("Practice")
# print(list)

'''Question 2: 
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
Example
: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format
The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.
Constraints
The elements added to the list must be integers.
Output Format
For each command of type print, print the list on a new line.
Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
'''Solution'''

# def listExpand(N):
#     list = []
    
#     for i in range(N):
#         i = input()
#         if i == print:
#             print(list)

# list =[]
# list.append(1)
# list.append(3)
# list.insert(2, 2)
# print(list)

# list.remove(3)
# print(list)

# list.append(14)
# list.append(11)
# list.append(9)
# print(list)

# list.sort()
# print(list)

# list.pop()
# print(list)

# list.reverse()
# print(list)

# if __name__ == '__main__':
#     N = int(input())
#     listExpand(N)











'''Question 3: print element using for loop?'''
# A = ['a','b','c','d','e']
# for i in A:
#     print(i)

'''Question 4: '''
# print([1,2,3,4] == [4,3,2,1])
# print(	[6,4,4,4] >  [6])






# #Initialize matrix a  
# a = [1,2,3,4] 
   
# #Initialize matrix b  
# b = [4,3,2,1]
   
# flag = True
   
# #Calculates number of rows and columns present in first matrix  
# row1 = len(a)
# col1 = len(a[0])
   
# #Calculates number of rows and columns present in second matrix  
# row2 = len(b)
# col2 = len(b[0])

# #Checks if dimensions of both the matrices are equal  
# if(row1 != row2 or col1 != col2):  
#     print("Matrices are not equal")
   
# else:  
#     for i in range(0, row1):  
#         for j in range(0, col1):  
#             if(a[i][j] != b[i][j]):  
#                 flag = False
#                 break
      
#     if(flag):  
#         print("Matrices are equal")
#     else:  
#         print("Matrices are not equal")




# def listExpand(N):
#     list = []
#     if N == int:
#         print(N, "commond will run")
#         input(list)*N

# if __name__ == '__main__':
#     N = int(input())
#     listExpand(N)

# def listExpand():
#     list = [3,4,5,8]

#     # for i in range(N):
#     #     i = input()
#     #     if i == print:
#     #         print(list)

#     if input() == print:
#         print(list)
    
# if __name__ == '__main__':
#     # N = int(input())
#     listExpand()


# a = int(input())
# b = int(input())
# s = (a+b)
# # print(s)
# print()

# def listExpand(N):
#     list = []
    
#     for i in range(N):
#         i = input()
    
# if __name__ == '__main__':
#     N = int(input())
#     listExpand(N)

# list = [10,9,8,7,6,5,4,3,2,1]

# def inp(a,b,c):
    
    
# N = int(input())
# for i in range(N):
#     i = input()
#     s = "print"
#     if i == s:
#         print(list)
#     if 


# Reverce
# b = "Practice question of list in python"
# print(b[-2:-5:-1])

# b = "Practice question of list in python"
# print(b[1:7:2])
# print(b[-5:])
# print(b[:-5])
# print(b[-2:-8:-2])


# def inpt(a,b,c=None):
#     print(f'{a}({b}{c})')


# if __name__ == '__main__':
#     N = int(input())
    
#     def listExpand(N):
#         list = []
        
#         for P in range(N):
#             P = input().split(" ")
            # a = P[-1]
            # temp = []

            # if P[0] == "insert":
            #     list.insert(int(P[1]), (P[2]))
            # elif P[0] == "remove":
            #     list.remove(P[1])
            # elif P[0] == "append":
            #     list.append(int(P[1]))
            # elif P[0] == "sort":
            #     list.sort()
            # elif P[0] == "pop":
            #     list.pop()
            # elif P[0] == "reverse":
            #     list.reverse()
            # elif P[0] == "print":
                # print(list)
                # a = print(int(list))
            # else:
                # print("Enter a valid input")
                # listExpand(N)
# listExpand(N)



'''Q1. Write a function find(name) in python to display all the names from a list of names which are starting from alphabet 'p'.'''

# list = ["kishor", "Shubham", "pooja", "digvijay", "Rathod"]
# def searchName():
#     for i in list:
#         if i[0] == "p" or i[0] == "P":
#             print(i)
    
# searchName()


''' Q2. Write a function disp(name) in python to display all the names from a list of names whose length is of four characters.'''

'''check if a list contain element'''
# l1 = [2, 3, 4, 5, 5, 6, 7, 8 , 'f', 'l', 'y']
# print('l' in l1)

'''Q3. How to iterate over 2+ lists at the same time'''
name = ["pol", "Kishor", "shivam", "dinesh"]
animal = ["fish", "dog", "cat", "bear"]
age = [7, 8, 5, 9]

z =zip(name, animal, age)

for name, animal, age in z:
    print