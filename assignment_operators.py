# "=" is an assignment operator which assigns value to variable
banana_price = 4
# "+=" is an addition assignment operator. it is the short form of:
a = 4
a = a + 7
print(a)
b = 10
b += 5
print(b)
# now more interesting example:
user_age = int(input("How old are you? "))
years_user_cut = int(input("Nah, you don't look like " + str(user_age) + ". Tell me the truth, how many years "
                           "you cut off when you were telling me your age? "))
user_age += years_user_cut
print("Oh, so you are " + str(user_age))
