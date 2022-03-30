# variable is a sort of container where we store data values to make it easier to manage


print("Bitcoin market capitalisation is around $800 000 000")
print("Today price of Bitcoin is at around $42 000 US")
print("Market decided that Bitcoin is the most valuable cryptocurrency at the moment")
print("At current price of $42000 per unit, bitcoin holds strong fundamentals ")

# This is valid python program and this looks great. But if we want to change this to let us say to ethereum
# we have to manually change everything. Imagine how difficult it would be if the text is thousands of lines.
# to create variable we need to give it a name.

print("__________________This is to divide the text ____________________________________________________")

cryptocurrency = "Bitcoin"
price = 42000
position_in_the_market = "the most"
market_cap = 800000000

print(cryptocurrency + " market capitalisation is around  $" + str(market_cap))
print("Today price of " + cryptocurrency + " is at around $" + str(price) + ".")
print("Market decided that " + cryptocurrency + " is " + position_in_the_market + " valuable cryptocurrency "
                                                                                  "at the moment")
print("At current price of $" + str(price) + " per unit, " + cryptocurrency + " holds strong fundamentals ")

# Now lets change the value of these variables

cryptocurrency = "Ethereum"
price = "$3 000"
position_in_the_market = "the second most"
market_cap = "$360 000 000"

print("__________________This is to divide the text ____________________________________________________")

print(cryptocurrency + " market capitalisation is around  " + market_cap)
print("Today price of " + cryptocurrency + " is at around " + price + ".")
print("Market decided that " + cryptocurrency + " is " + position_in_the_market + " valuable cryptocurrency "
                                                                                  "at the moment")
print("At current price of " + price + " per unit, " + cryptocurrency + " holds strong fundamentals ")

# a boolean value is a True or False value

is_male = True
is_tasty = False

print(9 > 10)
print(9 == 10)
print(9 < 10)
# If the name of variable consists of two or more words, use underscores to separate them. By the way, we cannot use
# spaces or other symbols in variable names (only alphabets, numbers and underscore but cannot start with numbers)
# By the way, variable names are case-sensitive.
