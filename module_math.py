# Python has a built-in module that you can use for mathematical tasks.
# The math module has a set of methods and constants.
# math.ceil() Rounds a number up to the nearest integer.
import math
print(math.ceil(1.4))
print(math.ceil(5.3))
print(math.ceil(-5.3))
print(math.ceil(22.6))
print(math.ceil(10.0))
# math.ceil() method returns integer:
balance = math.ceil(-4.900)
print("math.ceil() returns integer value:", isinstance(balance, int))

# math.floor() 	Rounds a number down to the nearest integer
print("Floor function of 0.6 returns:", math.floor(0.6))
print("Floor function of 1.4 returns:", math.floor(1.4))
print("Floor function of 5.3 returns:", math.floor(5.3))
print("Floor function of -5.3 returns:", math.floor(-5.3))
print("Floor function of 22.6 returns:", math.floor(22.6))
print("Floor function of 10.0 returns:", math.floor(10.0))
# floor method returns int value:
x = math.floor(-3.2)
print("Math floor function of -3.2 returns integer value:", isinstance(x, int))

# math.fabs() Returns the absolute value of a number.
print(math.fabs(-66.43))
print(math.fabs(-7))
# The math.fabs() method returns the absolute value of a number, as a float.
# Absolute denotes a non-negative number. This removes the negative sign of the value if it has any.
# Unlike Python abs(), this method always converts the value to a float value.
distance = math.fabs(-250.6)
print("math.fabs returns float value", isinstance(distance, float), "which is", distance)

# math.factorial() 	Returns the factorial of a number
print(math.factorial(9))
print(math.factorial(6))
print(math.factorial(12))
# The math.factorial() method returns the factorial of a number.
# Note: This method only accepts positive integers.
# The factorial of a number is the sum of the multiplication, of all the whole numbers, from our specified number
# down to 1. For example, the factorial of 6 would be 6 x 5 x 4 x 3 x 2 x 1 = 720

# math.isinf() Checks whether a number is infinite or not.
print("The result of 10 divided by 3 is infinite number", math.isinf(10/3))

# math.pow() Returns the value of x to the power of y
print("4 raised to the power of 3 is", math.pow(4, 3))
print("56 is infinite number", math.isinf(56))
print("-45.34 is infinite number", math.isinf(-45.34))
print("+45.34 is infinite number", math.isinf(+45.34))
print("math.inf is infinite number", math.isinf(math.inf))
print(math.isinf(float("nan")))
print(math.isinf(float("inf")))
print(math.isinf(float("-inf")))
print("-math.inf is infinite number", math.isinf(-math.inf))

# math.fsum() Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
print(math.fsum([1, 2, 3, 4, 5]))
print(math.fsum([100, 400, 340, 500]))
print(math.fsum([1.7, 0.3, 1.5, 4.5]))

# math.gcd() 	Returns the greatest common divisor of two integers
print("Greatest common divisor of 14 and 35 is", math.gcd(14, 35))

# math.prod() Returns the product of all the elements in an iterable.
sequence = (2, 3, 4)
print("The product of sequence (2, 3, 4) is", math.prod(sequence))

# math.sqrt() Returns the square root of a number
print("Square root of 9 is", math.sqrt(9))
# returns float value

# math.isqrt() 	Rounds a square root number downwards to the nearest integer.
