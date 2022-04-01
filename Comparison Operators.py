""" Comparison operators are:
==  equal
!=  not equal
>   greater than
<   smaller than
>=  greater than or equal to
<=  smaller than or equal to
"""

print("10 is greater than 5: ", 10 > 5)

# you can compare string too. (lexicographically)

print("Alphabetical number of a letter \"a\" is greater than alphabetical number of a letter \"d\": ", "a" > "d")
print("Adam" < "Ann")

# You can chain multiple conditional statements in an if statements using boolean (comparison) operators:
grade = 88
if 70 <= grade <= 100:
    print("Passed")
