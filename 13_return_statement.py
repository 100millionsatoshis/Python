"""
Certain functions, such as int or str, return a value that can be used later. To do this for your defined functions,
you can use return statement.

return keyword allows us return information from a function
"""


def cube(num):
    return num*num*num


print(cube(4))
result = cube(5)
print(result)

# return keyword is the last thing in the function. Python does not execute anything that comes after the return key.


def biggest_num(x, y):
    if x >= y:
        return x
    else:
        return y


print(biggest_num(4, 7))
z = biggest_num(8, 5)
print(z)

# the function below compares the lengths of its arguments and returns the shortest one.


def shortest_string(x, y):
    if len(x) <= len(y):
        return x
    else:
        return y


print(shortest_string("banana", "apple"))
# Once you return a value from a function, it immidiately stops being executed. Any code after the return statement
# will never happen

