'''You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen'''
'''Solution: '''

def split_and_join(line):
    # write your code here
    x = line.split(" ")
    y = "-".join(x)
    return y

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)