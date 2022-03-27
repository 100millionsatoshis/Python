# Integers are numbers without decimal parts. For example, 5, -11, 0, 12, etc.
# floats are numbers with decimal parts.
print(7)
print(7.4677)
print(-7.25)
# "+" is python arithmetic operator called addition. 7 and 3.5 are called operands.
print(7 + 3.5)
# "-" is python arithmetic operator called subtraction
print(7 - 9.3)
# "*" is python arithmetic operator called multiplication
print(12 * 12)
# "/" forward slash is an arithmetic operator called division
print(10 / 3)
# "%" (percentage sign) is an arithmetic operator called modulo. (sometimes it is called remainder)
# The Python modulo operator calculates the remainder of dividing two values. The first number is divided
# by the second then the remainder is returned.
print(10 % 3)
# "**" is an arithmetic operator called exponentiation. It takes 1st number and multiplies it as many times as
# indicated in the 2nd number.
print(2**3)
# "//" is an arithmetic operator called floor division or quotient.
print("floor division 9//3 =", 9//3)
# arithmetic operators are executed "first came, first served" basis
print(2 * 3 + 4)
# unless you separate them with parenthesis
print(2 * (3 + 4))

my_number = -8
print(abs(my_number))
print(pow(2, 256))
print(max(3, 7, 200, -300))
print(min(3, 7, 200, -300))
print(round(6.5))
from math import *
print(floor(8.99))
print(ceil(6.601))
print(sqrt(82))
