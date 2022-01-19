
if __name__ == '__main__':
    N = int(input())
    list = []
        
    for P in range(N):
        P = input().split(" ")

        if P[0] == "print":
            print(list)
        # P[-1] = print(list)
        if P[0] == "insert":
            list.insert(int(P[1]), int(P[2]))
        elif P[0] == "append":
            list.append(int(P[1]))
        elif P[0] == "remove":
            list.remove(int(P[1]))
        elif P[0] == "sort":
            list.sort()
        elif P[0] == "pop":
            list.pop()
        elif P[0] == "reverse":
            list.reverse()