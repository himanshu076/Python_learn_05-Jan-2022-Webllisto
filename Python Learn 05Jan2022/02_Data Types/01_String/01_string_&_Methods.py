"""String"""
'''"Definition" In Python, string is an immutable sequence data type. It is the sequence of Unicode characters wrapped inside single, double, or triple quotes. ... If a string literal required to embed double quotes as part of a string then, it should be put in single quotes.'''

# # 1.
# String1 = 'Welcome to the new world'
# print("String with the use of single Quoyes: ")
# print(String1)

# # 2.
# String1 = "Welcome to the new world"
# print("\nString with the use of Double Quoyes: ")
# print(String1)

# # 3.
# String1 = '''Welcome to the new "world"'''
# print("\nString with the use of Triple Quoyes: ")
# print(String1)

# 4.
# String1 = '''Welcome 
#             to the 
#             new "world"'''
# print("\nString with the use of MultiLine Quoyes: ")
# print(String1)

# *********************************************************************************

# Python Program to Access
'''Access characters of String in python'''
 
# String1 = "GeeksForGeeks"
# print("Initial String: ")
# print(String1)
 
# # Printing First character
# print("\nFirst character of String is: ")
# print(String1[0])
 
# # Printing Last character
# print("\nLast character of String is: ")
# print(String1[-1])

# *********************************************************************************
'''String Slicing'''

# Printing 3rd to 12th character
# String1 = "GeeksForGeeks"
# print("\nSlicing characters from 3-12: ")
# print(String1[3:12])
 
# Printing characters between
# 3rd and 2nd last character
# print("\nSlicing characters between " +
#     "3rd and 2nd last character: ")
# print(String1[3:-2])

# *********************************************************************************
'''Deleting/Updating from a string'''
# 1.
# Updating a character of the String
# String1 = "Hello, I'm a Geek"
# String1[2] = 'p'
# print("\nUpdating character at 2nd Index: ")
# print(String1) # Throw error

# 2.
# Updating Entire String
# String1 = "Hello, I'm a Geek"
# String1 = "Welcome to the Geek World"
# print("\nUpdated String: ")
# print(String1)

"""Method How to replace characters in a string in Python"""
# 1.
# a_string = "aba"
# a_string = a_string.replace("a", "b")
# print(a_string)

# 2.
# old_string = "aba"

# string_list = list(old_string)
# string_list[2] = "c"

# new_string = "".join(string_list)
# print(new_string)

# *********************************************************************************
'''Deletion od character'''
# 1.
# Deleting a character
# of the String
# String1 = "Hello, I'm a Geek"
# del String1[2]
# print("\nDeleting character at 2nd Index: ")
# print(String1) # throw an error

# 2.
# Deleting Entire String with the use of del
# String1 = "Hello, I'm a Geek"
# del String1
# print("\nDeleting entire String: ")
# print(String1)

# *********************************************************************************
'''Escape Sequencing in Python'''

# 1. Initial String
# String1 = '''I'm a "Geek"'''
# print("Initial String with use of Triple Quotes: ")
# print(String1)
 
# 2. Escaping Single Quote
# String1 = 'I\'m a "Geek"'
# print("\nEscaping Single Quote: ")
# print(String1)
 
# 3. Escaping Double Quotes
# String1 = "I'm a \"Geek\""
# print("\nEscaping Double Quotes: ")
# print(String1)
 
# Printing Paths with the use of Escape Sequences
# String1 = "C:\\Python\\Geeks\\"
# print("\nEscaping Backslashes: ")
# print(String1)

# *********************************************************************************
'''To ignore the escape sequences in a String, r or R is used, this implies that the string is a raw string and escape sequences inside it are to be ignored.'''


# Printing Geeks in HEX
# String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print("\nPrinting in HEX with the use of Escape Sequences: ")
# print(String1)
 
# Using raw String to
# ignore Escape Sequences
# String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print("\nPrinting Raw String in HEX Format: ")
# print(String1)

# *********************************************************************************
'''Formatting of Strings'''

# Default order
# String1 = "{} {} {}".format('Geeks', 'For', 'Life')
# print("Print String in default order: ")
# print(String1)
 
# Positional Formatting
# String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
# print("\nPrint String in Positional order: ")
# print(String1)
 
# Keyword Formatting
# String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
# print("\nPrint String in order of Keywords: ")
# print(String1)

'''Integers such as Binary, hexadecimal, etc., and floats can be rounded or displayed in the exponent form with the use of format specifiers. '''
# Formatting of Integers
# String1 = "{0:b}".format(16)
# print("\nBinary representation of 16 is ")
# print(String1)
 
# Formatting of Floats
# String1 = "{0:e}".format(165.6458)
# print("\nExponent representation of 165.6458 is ")
# print(String1)
 
# Rounding off Integers
# String1 = "{0:.2f}".format(1/6)
# print("\none-sixth is : ")
# print(String1)

'''string can be left() or center(^) justified with the use of format specifiers, separated by a colon(:)'''
# String alignment
# String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'for', 'Geeks')
# print("\nLeft, center and right alignment with Formatting: ")
# print(String1)
 
# To demonstrate aligning of spaces
# String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
# print(String1)

'''Old style formatting was done without the use of format method by using % operator'''
# Python Program for Old Style Formatting of Integers
 
# Integer1 = 12.3456789
# print("Formatting in 3.2f format: ")
# print('The value of Integer1 is %3.2f' % Integer1)
# print("\nFormatting in 3.4f format: ")
# print('The value of Integer1 is %3.4f' % Integer1)