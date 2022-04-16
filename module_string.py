# capitalize()	Converts the first character to upper case

a = "hello"
print(a.capitalize())
b = "world"
print(a.capitalize(), "world".capitalize())

# the 'casefold()' method converts string into lower case

c = "LONDON"
print(c.casefold())
print(c.casefold().capitalize())
d = "TokiYO"
print(d.casefold().capitalize())
print(d.casefold().capitalize(), "IS THE CApitaL of".casefold(), "United States".casefold().capitalize())
# center()	Returns a centered string
e = "Chapter One"
print(e.center(90))


# count()	Returns the number of times a specified value occurs in a string
f = "North Korea is sitting on 200 million worth of unmixed cryptocurrencies. Bitcoin mining is developed in Iran"
print(f.count("c"))
print("North Korea is sitting on 200 million worth of unmixed cryptocurrencies. "
      "Bitcoin mining is developed in Iran".count("o"))


# encode()	Returns an encoded version of the string
txt = "My name is Ståle"
x = txt.encode()
print(x)
# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
txt = "My name is Ståle"

print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))


# endswith() Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
# expandtabs()	Sets the tab size of the string
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)

# find()	Searches the string for a specified value and returns the position of where it was found
print("This is text and it contains the word bomb and my code should be able to find it".find("bomb"))

# format()	Formats specified values in a string
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)

# index()	Searches the string for a specified value and returns the position of where it was found

txt = "Hello, welcome to my world."
x = txt.index("welcome")
z = txt.find("welcome")
print(x)
print(z)
"""
The index() method finds the first occurrence of the specified value.
The index() method raises an exception if the value is not found. 
The index() method is almost the same as the find() method, the only difference is that the find() method returns
-1 if the value is not found.
"""
h = "Let's read books and do sports"
print(h.find("bomb"))


# Fill the string with zeros until it is 10 characters long:
txt = "50"
x = txt.zfill(10)
print(x)
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.
