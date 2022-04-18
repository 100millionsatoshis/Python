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
