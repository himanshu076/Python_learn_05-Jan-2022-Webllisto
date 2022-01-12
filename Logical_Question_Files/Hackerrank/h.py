# l1 = "1,0,1,0,1,0,1,0,0, 0, 0, 0, 1, 1, 1, 1"
# # print(l1[::-1])
# l2 = '0'
# l3 = '1'

# # l1.reverse(1, 0)
# # l1.reverse()
# # print(l1)

# l1.swapcase()
# print(l1)

# def untercgabg_unteg():

def swap(x,y): 
    print('Before swapping a :',x)
    print('Before swapping b :',y)
    #logic to swap without using third variable 
    x,y=y,x
    return x,y 


a=int(input("Enter value : "))
b=int(input("Enter value : "))    
a,b=swap(a,b) 
print("After swapping a becomes :",a)
print("After swapping b becomes :",b)

