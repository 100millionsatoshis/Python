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
x = txt.expandtabs(5)
print(x)

# find()	Searches the string for a specified value and returns the position of where it was found
print("This is text and it contains the word bomb and my code should be able to find it".find("bomb"))

# format()	Formats specified values in a string
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
# format_map() does the same thing

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

# isalnum() checks if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)
"""
The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and 
numbers (0-9).
Example of characters that are not alphanumeric: (space)!#%&? etc.
"""
txt = "Company 12"
x = txt.isalnum()
print(x)

# isalpha()	Returns True if all characters in the string are in the alphabet.
txt = "CompanyX"
x = txt.isalpha()
print(x)
# The isalpha() method returns True if all the characters are alphabet letters (a-z).
# Example of characters that are not alphabet letters: (space)!#%&? etc.
txt = "Company10"
x = txt.isalpha()
print("Company10 is alphabetic:", x)

# isascii()	Returns True if all characters in the string are ascii characters
txt = "Company123"
x = txt.isascii()
print("Company123 are isascii characters: ", x)
# The isascii() method returns True if all the characters are ascii characters  (a-z).

# isdecimal()	Returns True if all characters in the string are decimals
txt = "\u0033"  # unicode for 3
x = txt.isdecimal()
print(x)
# The isdecimal() method returns True if all the characters are decimals (0-9).
# This method is used on unicode objects.

# isdigit()	Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print("50800 are digits:", x)
# The isdigit() method returns True if all the characters are digits, otherwise False.
# Exponents, like ², are also considered to be a digit.

# isidentifier() Returns True if the string is an identifier
ab = "MyFolder"
bc = "Demo002"
cd = "2bring"
de = "my demo"
print(ab.isidentifier())
print(bc.isidentifier())
print(cd.isidentifier())
print(de.isidentifier())
"""
The isidentifier() method returns True if the string is a valid identifier, otherwise False.
A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or 
underscores (_). A valid identifier cannot start with a number, or contain any spaces.
"""

# islower()	Returns True if all characters in the string are lower case
txt = "hello world!"
x = txt.islower()
print(x)

# isnumeric() Returns True if all characters in the string are numeric.
"""
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
Exponents, like ² and ¾ are also considered to be numeric values.
"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and 
the - and the . are not.
"""
txt = "565543"
x = txt.isnumeric()
print("565543 is numeric:", x)

# isprintable()	Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
# The isprintable() method returns True if all the characters are printable, otherwise False.
# Example of none printable character can be carriage return and line feed.
# Remove spaces at the beginning and at the end of the string:

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)

# isspace()	Returns True if all characters in the string are whitespaces
txt = "   "
x = txt.isspace()
print(x)

# istitle() Returns True if the string follows the rules of a title:
# Checks if each word start with an upper case letter:
# The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the
# word are lower case letters, otherwise False.


# isupper()	Returns True if all characters in the string are upper case

# join() Converts the elements of an iterable into a string.
# Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.



txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

# Fill the string with zeros until it is 10 characters long:
txt = "50"
x = txt.zfill(10)
print(x)
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.
