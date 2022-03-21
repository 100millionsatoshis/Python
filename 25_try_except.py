try:

    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("You cannot divide into 0")
except ValueError:
    print("Invalid input")

# these commands help us to manage errors. Instead of whole code getting broken, we get custom error messages.
# we also can store the error as variable.
# not specifying a type of error gives you "too broad" type of warning, not error.
try:
    result = 5/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as dabdala:
    print(dabdala)
except ValueError:
    print("Invalid input")
