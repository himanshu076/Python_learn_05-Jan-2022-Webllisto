'''All Methods One by one'''

'''Capatilize()'''
# txt = "hello, and welcome to my world."
# x = txt.capitalize()
# print (x)

'''casefold()'''
# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x)

'''center()'''
# txt = "banana"
# x = txt.center(20)
# print(x)

'''count()'''
# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple")
# print(x)

# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple", 10, 24)
# print(x)

'''encoded()'''
# UTF-8 encode the string:
# txt = "My name is Ståle"
# x = txt.encode()
# print(x)

'''endswith()'''
# txt = "hello, and welcome to my world."
# t = txt.endswith("rld.")
# print(t)

'''expandtabs()'''
# txt = "H\te\tl\tl\to"
# t = txt.expandtabs()
# print(t)

'''find()'''
# txt = "hello, and welcome to my world."
# t = txt.find("world")
# print(t)

'''format()'''
# txt = "for only {price:.2f} dollars!"       # "2f" is used for float or 2 decimal place
# print(txt.format(price = 599))

'''format_map()'''
# txt = "for only {price:.2f} dollars!"       # "2f" is used for float or 2 decimal place
# print(txt.format(price = 599))

'''index()'''
# txt = "hello, and welcome to my world."
# t = txt.index("to")
# print (t)

'''isalnum()'''
# txt = "Company12"
# x = txt.isalnum()
# print(x)

'''isalpha()'''
# txt = "bjhdcdbnjncdbv"
# x = txt.isalpha()
# print(x)

'''isascii()'''
# txt = "Company1235"
# x = txt.isascii()
# print(x)u0033

'''isdecimal()'''
# txt = "\u0033"
# x = txt.isdecimal()
# print(x)

'''isdigit()'''
# txt = "26562"
# x = txt.isdigit()
# print(x)

'''isidentifier()'''
# txt = "Demo"
# x = txt.isidentifier()
# print(x)

# a = "MyFolder"
# b = "Demo002"
# c = "2bring"
# d = "my demo"
# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

'''islower()'''
# txt = "csvcghvsjh"
# x = txt.islower()
# print(x)

# a = "Hello World!"
# b = "hello 123"
# c = "mynameisPeter"
# print(a.islower())
# print(b.islower())
# print(c.islower())

'''isnumeric()'''
# txt = "51156123"
# x = txt.isnumeric()
# print(x)

# a = "\u0030"
# b = "\u00B2"
# c = "10km2"
# d = "-1"
# e = "1.5"
# print(a.isnumeric())
# print(b.isnumeric())
# print(c.isnumeric())
# print(d.isnumeric())
# print(e.isnumeric())

''' isprintable'''
# txt = "Hello! How are you #1?"
# x = txt.isprintable()
# print(x)

# txt = "Hello! \nare you #1?"
# x = txt.isprintable()
# print(x)

'''isspace()'''
# txt = "   "
# x = txt.isspace()
# print(x)

'''istitle()'''
# txt = "Hello, And Welcome To My World!"
# x = txt.istitle()
# print(x)

# a = "HELLO, AND WELCOME TO MY WORLD"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

'''isupper()'''
# txt = "THIS IS NOW!"
# x = txt.isupper()
# print(x)

'''join()'''
# myTuple = ("Jhon", "peter", "Vicky")
# x = "#".join(myTuple)
# print(x)

# myDict = {"name":"shubham", "country":"Duabi"}
# mySeperator = " TEST "
# x = mySeperator.join(myDict)
# x = mySeperator.join(mySeperator)
# print(x)  

'''ljust()'''
# txt = "banana"
# x = txt.ljust(20)
# print(x)

# txt = "banana"
# x = txt.ljust(20, "O")
# print(x)

'''lower()'''
# txt = "HELLO my FRIENDS!"
# x = txt.lower()
# print(x)

'''lstrip()'''
# txt = "     banana     "
# x = txt.lstrip()
# print("Ding - Ding", x, "ding - ding")

# txt = ".....,,,,,gggssstt.......banana..."
# x = txt.lstrip(".,gst")
# print(x)

'''maketrans()'''
# txt = "Hello Sam!"
# mytable = txt.maketrans("S", "P")
# print(txt.translate(mytable))

# txt = "Hi Sam!"
# x = "mSa"
# y = "eJo"
# mytable = txt.maketrans(x, y)
# print(txt.translate(mytable))

# txt = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = txt.maketrans(x, y, z)
# print(txt.translate(mytable))

'''partition()'''
# txt = "I could eat bananas all day"
# x = txt.partition("bananas")
# print(x)

# txt = "I could eat bananas all day"
# x = txt.partition("apples")
# print(x)

'''replace()'''
# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)

'''rfind()'''    # it catches last occurance of the searched
# txt = "mi casa, su casa"
# x = txt.rfind("casa")
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.rfind("e")
# print(x)

'''rindex()'''
# txt = "mi casa, su casa"
# x = txt.rindex("casa")
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.rfind("e")
# print(x)

'''rjust()'''
# txt = "banana"
# x = txt.rjust(20)
# print(x)

# txt = "banana"
# x = txt.rjust(20, "O")
# print(x)

'''rpartitation()'''
# txt = "T could eat bananas all day, bananas are my favotite fruit"
# x = txt.rpartition("bananas")
# print(x)

'''rsplit()'''
# txt = "apple, banana, mango"
# x = txt.rsplit(", ")
# print(x)

'''rstrip()'''
# txt = "     banana     "
# x = txt.rstrip()
# print("bhdbu", x, "bhbjk")

'''split()'''
# txt = "welcomwe to the jungle"
# x = txt.split()
# print(str(x))

'''splitlines()'''
# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines()
# print(x)

# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines(True)
# print(x)

'''startswith()'''
# txt = "Hello, Welcome to my world"
# x = txt.startswith("Hello")
# print(x)

'''strip()'''
# txt = "     banana     "
# x = txt.strip()
# print("svjsjh", x, s"sybskj")

'''swapcase()'''
# txt = "Hello My Name Is PETER"
# x = txt.swapcase()
# print(x)

'''title()'''
# txt = "Welcome to my 2nd world b2b2b2 and g3g3g3"
# x = txt.title()
# print(x)

'''translate()'''    # or use it with maketrans
# mydict = {83 : 80}
# txt = "Hello Sam!"
# print(txt.translate(mydict))

'''upper()'''
# txt = "Hello my friends!"
# x = txt.upper()
# print(x)

'''zfill()'''
# txt = "50"
# x = txt.zfill(10)
# print(x)

# a = "hello"
# b = "welcome to the jungle"
# c = "10.000"

# print(a.zfill(10))
# print(b.zfill(10))
# print(c.zfill(10))

