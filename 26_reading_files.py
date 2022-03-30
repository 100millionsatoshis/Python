# The key function for working with files in Python is the open() function
# the open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""
open("26_countries.txt")

"""
In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""


# One more mode is # r+ which means read and write

# now we make sure if file is readable.
producers = open("random folder/26_producers.txt", "r")
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

laptops = open("random folder/26_producers.txt")
for laptop in laptops.readlines():
    print(laptop)

# photo = open("random folder/GOPR0528.JPG", "r")
# print(photo.read())
# photo.close()

# Our little experiment showed that python did not read JPEG file.
# we continue experimenting by moving JPEG file to the same folder as python file.
# we get the same unicode decoder error.
# putting text file into subdirectory breaks the code.

# now it is time experiment with other types of files
# orderbook = open("2022.xlsx", "r")
# print(orderbook.read())
# orderbook.close()
# we get the same "unicodedecodererror" as with jpeg file extension
