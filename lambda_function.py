# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:
# Add 10 to argument "a", and return the result:
x = lambda a: a + 10
print(x(5))
# Multiply argument a with argument b and return the result:
y = lambda a, b: a * b
print(y(5, 6))
# Summarize argument a, b, and c and return the result:
z = lambda a, b, c: a + b - c
print(z(5, 6, 2))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an
# unknown number:


def myfunc(n):
    return lambda a: a * n


# Use that function definition to make a function that always doubles the number you send in:
my_doubler = myfunc(2)
# now variable my_doubler is equal to lambda a: a * 2
# lambda has no parameter yet. In the next line print function passes parameter 11 to lambda.
print(my_doubler(11))

string = 'some kind of a useless lambda'
print(lambda string: print(string))

text = "some text"
lambda text: print(text)

text2 = "random text"
(lambda text2: print(text2))(text2)
