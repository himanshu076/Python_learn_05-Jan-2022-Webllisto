
class sampleSecond():
    # print("priniting from second file {}".format(__name__))

    def value_Of_Second_X(x):
        print(x)

    def value_Of_Second_y(y):
        print(y)



if __name__=="__main__":
    print("File second executed when ran directly")
    print("File second ececuted when imported")


# print("name", __name__)
# print("locaion", __file__)