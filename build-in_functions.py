# abs()	Returns the absolute value of a number
x = abs(-7.25)
print(x)
y = abs(3+5j)
print(y)
print(isinstance(y, float))

# build-in abs() function may not always return float value. This needs more clarification.

# float() Returns a floating point number
a = float(3)
print("3 converted into floating point number is", a)
# A number or a string that can be converted into a floating point number.
print(float("-3.5"))
# String can be converted only a number is stored as string
print(float("inf"))
