"""
Code reuse is a very important part of programming in any language. Increasing code size makes it hard to maintain.
For a large programming project to be successful, it is essential to abide by the "Don't Repeat Yourself", or DRY,
principle. We have already looked at one way of doing this: by using loops. There are two more ways, functions and
modules.
Bad, repetitive code is said to abide by the WET principle, which stands for Write Everything Twice, or We Enjoy Typing.

Function is a collection of code, which performs a specific task.
We can take a bunch of lines of code that do one thing and put them inside function.
And then we want to that task or that one thing that function was doing, we can just call the function.
Functions can help us to organize our code better. It allows us to break up our code into little chunks that are doing
different things. Functions are a core concept when we talk about programing in python.

Any statement that consists of a word followed by information in parentheses is a function call.
Here are some examples:
print("Hello World")
range(2, 20)
str(12)
range(10, 20, 3)

The word in front of the parentheses are function names, and comma-separated values inside the parentheses are
function arguments.
In addition to using pre-defined functions, you can create your own functions by using the def statement.
Here is an example of a function called my-func. It takes no arguments, and prints "spam" 3 times. It is defined
and then called. The statements in the function are executed only when the function is called.
"""


def my_func():
    print("spam")
    print("spam")
    print("spam")


# functions will not execute itself automatically. We have to call them. The code block within every function starts
# with a colon (:) and is indented. 

my_func()


# we can give functions parameter.


def send_invitation(name, event):
    print("Dear" + name + ", We would like to invite you to " + event)


send_invitation("Tom", "birthday party")
