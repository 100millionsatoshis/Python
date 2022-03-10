def biggest_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(biggest_num(-100, 6, 100))

# == means equal, != means not equal, > means greater than, < means less than
# strings also can be compared
