# this lesson is about reading from external files in python
# it can a text file or csv file or a html file. For that you can use something called python read command.

# open("countries.txt", "read")

# after name of the file we can indicate mode, such as: "r", stand for read,
# "w" stands for write and "a" which stand for append.
# One more mode is # r+ which means read and write
# Now we save file as variable

countries = open("countries.txt", "r")
print(countries)
# this did not work.
# now we make sure if file is readable.
print(countries.readable())

# once you open a file, make sure to close it once you are done with it.
countries.close()

# below I show an example of readable giving us false result due to file open mode is w
# countries_and_its_capitals = open("countries.txt", "w")
# print(countries_and_its_capitals.readable())
# countries.close()

countries_and_its_capitals = open("countries.txt", "r")
print(countries_and_its_capitals.read())
countries.close()

print("we can read first line by using readline function")

countries_and_its_capitals = open("countries.txt", "r")
print(countries_and_its_capitals.readline())
print(countries_and_its_capitals.readline())
countries.close()
