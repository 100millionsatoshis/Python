# this lesson is about reading external files in python
# it can be a text file or csv file or a html file. For that you can use something called python read command.

# open("26_26_countries.txt")

# after name of the file we can indicate mode, such as: "r", stand for read,
# "w" stands for write and "a" which stand for append.
# One more mode is # r+ which means read and write
# Now we save file as variable
# now we make sure if file is readable.
producers = open("26_producers.txt", "r")
print(producers.readable())
producers.close()

# if we set the mode to w and check it is readable we get False result

# these 3 lines of code below somehow deletes everything from a file.
# producers = open("26_producers.txt", "w")
# print(producers.readable())
# producers.close()

# once you open a file, make sure to close it once you are done with it.

# Now let us read the entire file:

list_of_countries = open("26_countries.txt", "r")
print(list_of_countries.read())
list_of_countries.close()

print("_____________________________________________")
# readline function gets first line from the file and moves the cursor to the next line
bucket_list = open("26_countries.txt", "r")
print(bucket_list.readline())
print(bucket_list.readline())
bucket_list.close()

print("______________________________________________")
# readlines function takes all the lines from the text and puts them into list
staff = open("26_employees.txt")
print(staff.readlines())
staff.close()

laptops = open("26_producers.txt")
for laptop in laptops.readlines():
    print(laptop)
