# strings is one of the most commonly used type of data in python.
# strings are basically just plain texts.
# strings in Python are surrounded either by single quotation marks, or double quotation marks.

print('Python is awesome')
print("Python is awesome")

# to move text to new line we use \n
print("Python is awesome \nIt is one of the most commonly used programming languages")

# to write quotation mark we use \ (backslash)
print("Russia's \"special operation\" in Ukraine costing it tons of money.")

# we use \t to make tab

print("March salary\t$10000\nApril Salary\t$12000")

# You can multipy string by a number

print("Multiply_sting" * 3)

# strings can be stored inside the variable
whatever_variable = "important information"
print(whatever_variable)

# concatenation is taking one string and appending another string
print(whatever_variable + " should store safely")

# we can use functions with strings:
# lowercase
name = "SATOSHI NAKOMOTO"
print(name.lower())

# uppercase
print(whatever_variable.upper())

# check if it is uppercase
print(whatever_variable.isupper())
print(name.isupper())
print(name.islower())

# now let's convert the string into uppercase and check if it is uppercase:
print(whatever_variable.upper().isupper())

# check the length of the string:
print(len(whatever_variable))

# in python, when start counting (indexing) we start with zero

print(name.index("O"))

# replace function

print(whatever_variable.replace("information", "info"))
"""
This 
is 
multiline string
"""
'''
This
is
multiline string 
too
'''

# Like in many other programming languages, strings in Python are arrays of bytes representing unicode caracters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1
# Square brackets can be used to access the elements of the string
a = "Banana is delicious"
print(a[7])

# since strings are arrays, we can loop through characters in a string, with a for loop.
for letters in "Banana":
    print(letters)

# to get the length of a string, use len() function.
m = "Rabbithole Diary"
print(len(m))
# To check if a certain phrase or character present in a string, we can use the keyword in
sms = "Dasha, send kids to grandparents and hide my gun"
print("gun" in sms)

# if statement
message = "Hi, I am Taliban member, I would to purchase some gun and pay with cocaine"
