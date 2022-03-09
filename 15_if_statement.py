# if statements are used to help our python program to make decision.

is_male = True

if is_male:
    print("You are a male")

is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")

is_sedan = False
is_german = True

if is_sedan and is_german:
    print("It is German sedan")
elif is_sedan and not is_german:
    print("It is sedan but not German")
elif not is_sedan and is_german:
    print("It is German but not sedan")
else:
    print("It is neither German nor sedan")

is_fruit = True
is_edible = True

if is_fruit or is_edible:
    print("It is food")
else:
    print("It is not food")
