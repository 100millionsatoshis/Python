# this lesson is about reading from external files in python
# it can a text file or csv file or a html file. For that you can use something called python read command.

# open("countries.txt", "read")

# after name of the file we can indicate mode, such as: "r", stand for read,
# "w" stands for write and "a" which stand for append.
# One more mode is # r+ which means read and write
# Now we save file as variable

countries = open("countries.txt")
# once you open a file, make sure to close it once you are done with it.

countries.close()
