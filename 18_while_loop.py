""" while loop is a structure in python which allows loop through and execute a block of code multiple times.
# we could specify a few different lines of code and put that code inside of while loop, and it would loop through that code
# executing it repeatedly until certain condition was false.
"""
i = 1
while i <= 7:
    print(i)
    i = i + 1
print("Done with loop")
"""
# i = i + 1  can be written as i += 1 which gives same effect but visually looks clean.
The code in the body of a while loop is executed repeatedly. This is called iteration. 
You can use multiple statements in a while loop. For example, you can use an if statement to make decisions. 
"""
x = 1
while x < 6:
    if x % 2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
    x += 1

number = int(input("Enter a number: \n"))
length = 0
while number > 0:
    number //= 10
    length += 1
print(length)

number1 = int(input("Write any number: "))
total = 0
while number > 0:
    num = number1 % 10
    total += num
    number1 //= 10
print(sum)
# To end a "while" loop prematurely, the break statement can be used. For example, we can break an infinite loop
# is some condition is met.
i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")

"""
"while True" is a short and easy way to make an infinite loop. 
An example use case of break: 
An infinite while loop can be used to continuously take user input. 
Another statement that can be used within loops is "continue"
Unlike "break", continue jumps back to the top of the loop, rather than stopping it. 
Basically, the continue statement stops the current iteration and continues within the next one. 
For example:
"""
m = 0
while m < 7:
    m += 1
    if m == 3:
        print("skipping 3")
        continue
    print(m)
# If the while loop condition is False before starting the first iteration, the while loop will not even start running. 
