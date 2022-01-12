'''You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.'''

'''Solution: '''

def swap_case(s):
    x = s.swapcase()
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)