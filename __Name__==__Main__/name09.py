from Second_of__name__10 import sampleSecond
class sampleFirst():
    print("priniting from first file {}".format(__name__))
    
    def value_Of_First_X(x):
        print(x)

    def value_Of_First_y(y):
        print(y)

# if __name__=="__main__":
print("File first executed when ran directly")
sampleSecond.value_Of_Second_X(10)

# else:
print("File first ececuted when imported")
print("name", __name__)

print("name", __name__)
print("locaion", __file__)