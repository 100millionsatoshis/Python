# Python allows for user input. That means we are able to ask user for input.
# input function prompts the user for input, and returns what they enter as sting (with contents automatically
# escaped).
level = input("what is your level?: ")
name = input("Enter your name: ")

# inside the parenthesis we write prompt. Let's assume we want to take the age of the user as input.
# We know input() function returns a string. To convert it to a number, we can use the int() function.

age = int(input("Enter your age: "))


print("Hello " + name + "! You are " + str(age) + " years old. You level is: " + level)

# walrus operator := allows you to assign values to variables within an expression, including variables that do not 
# exist yet. 
# instead of this: 
"""
color = str(input("what is your favorite color? "))
print(color)
"""
# you write this: 
print(color := str(input("what is your favorite color? ")))
