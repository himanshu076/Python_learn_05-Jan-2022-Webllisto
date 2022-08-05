
# Example 1:
# y = lambda x: x + 1
# print(y(2))

# Exapmle 2:
# full_name = lambda x, y: f'Full Name {x.title()} {y.title()}'
# print(full_name('guido', 'van rossum'))

# Exapmle 3:
# high_ord_func = lambda x, func : x + func(x)
# print(high_ord_func(2, lambda x:x*2))

# import dis
# add = lambda x,y : x+y
# # print(type(add))

# print(dis.dis(add))
# print(add)

# def add(x, y):
#     return x+y

# dis.dis(add)

# *****************************************************************************************
'''No Statements

A lambda function can't

 contain any statements. In a lambda function, statements like return'pass, assert, or raise will raise a SyntaxError exception. Here’s an example of adding assert to the body of a lambda:

>>> (lambda x: assert x == 2)(2)
  File "<input>", line 1
    (lambda x: assert x == 2)(2)
                    ^
SyntaxError: invalid syntax
This contrived example intended to assert that parameter x had a value of 2. But, the interpreter identifies a SyntaxError while parsing the code that involves the statement assert in the body of the lambda.'''

# *************************************************************************************
'''Single Expression

In contrast to a normal function, a Python lambda function is a single expression. Although, in the body of a lambda, you can spread the expression over several lines using parentheses or a multiline string, it remains a single expression:

>>> (lambda x:(x % 2 and 'odd' or 'even'))(3)
'odd'
The example above returns the string 'odd' when the lambda argument is odd, and 'even' when the argument is even. It spreads across two lines because it is contained in a set of parentheses, but it remains a single expression.'''
# y = lambda x: (x%2 and 'odd' or 'even')
# print(y(5))


