"""
Operator precedence is very important concept in programming. It is an extension of mathematical idea of order of
operations (multiplication being performed before addition, etc.) to include other operators, such as those in
Booelan logic.
The below code shows that == is higher precedence than or:
"""
print(False == True or True)
print(False == (False or True))
print((False == False) or True)

# Python's order of operations is the same as that of normal mathematics:
# parentheses first, then exponentiation, then multiplication/division, and then addition/subtraction.