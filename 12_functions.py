#Function is a collection of code which performs a specific task.
#We can take a bunch of lines of code that do one thing and put them inside of a function.
#And then we want to that task or that one thing that function was doing, we can just call the function.
#Functions can help us to organize our code better. It allows us to break up our code into little chunks that are doing
#different things. Functions are a core concept when we talk about programing in python.
def sayhi():
    print("hello world")

#functions will not execute itself automatically. We have to call them.

sayhi()

#we can give functions parameter.

def send_invitation(name, event):
    print("Dear" + name + ", We would like to invite you to " + event)

send_invitation("Tom", "birthday party")
