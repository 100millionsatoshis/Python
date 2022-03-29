# Booleans represent one of two values: True or False.
# In programming, you often need to know if an expressions is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns Boolean answer:
# example:
print(10 > 9)
print(10 == 9)
print(10 < 9)
# When you run a condition in an if statement, Python returns True or False:
a = 16
b = 109
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
# bool() function allows you to evaluate any value and give you True or False in return. Example:
print(bool("hello"))
print(bool(15))
# Most values are True
# Almost any value is evaluated to true if it has some sort of content.
# Any string is True, except empty string.
# Any number is True, except 0.
# Any list, tuple, set and dictionary are True, except empty ones.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some values are False:
# In fact, there are not many values that evaluate to False, except empty values such as (), [], {}, ""
# the number 0 and the value none. And of course the value False evaluates to False.
# The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool({})
bool([])
bool(())
# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a
# class with a __len__ function that returns 0 or False:


class MyClass:
    def __len__(self):
        return 0


my_object = MyClass()
print(bool(my_object))

# You can create a function that returns Boolean Value:


def myfunction():
    return True


print(myfunction())


def my_little_function():
    return False


if my_little_function():
    print("Yes")
else:
    print("No")
# python also has many build-in functions that return a boolean value, like isinstance() function, which can be used to
# determine if an object is of a certain data type:
# example. Check if an object is an integer or not:
a = 3490
print(isinstance(a, int))
