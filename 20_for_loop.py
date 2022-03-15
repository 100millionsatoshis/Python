# for loop is a special type of loop in python which allows us to loop over different collections of items.
# A lot of times we use for loops in python to loop through different arrays or letters inside of strings
# we can loop through a series of numbers. So, for loop provides specific purpose

for letter in "Rabbithole Diary":
    print(letter)

breakfast_options = ["scrambled_eggs", "sausages", "oatmeal"]
for my_options in breakfast_options:
    print(my_options)

for raqamlar in range(5):
    print(raqamlar)

for raqamlar in range(10, 15):
    print(raqamlar)

breakfast_menu = ["poached_egg", "scrambled_eggs", "sausages", "oatmeal"]
for ruyxat in range(len(breakfast_menu)):
    print(breakfast_menu[ruyxat])

# 1 more example:

for ruyxat in range(5):
    if ruyxat == 0:
        print("first iteration")
    else:
        print("Not first iteration")
