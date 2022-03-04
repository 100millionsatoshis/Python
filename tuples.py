#A Tuple is a type of data structure which basically means container where we can store different values.
# If you are familiar with lists in python, tuple is very similar to a list. It is basically a structure where we can
#store a multiple pieces of information. But a tuple has a couple key differences from lists.
#One of the most common examples of tupples is coordinates.

coordinates = (2000, 178, 80)

#Tuple is immutable which means a tuple cannot be changed or modified

print(coordinates)
print(coordinates[0])
print(coordinates[1:])
list_of_tuples = [(1, 2), (3, 4), (5, 6), (7, 8)]
another_list_of_tuples = [(9, 10), (11, 12)]
print(list_of_tuples)
list_of_tuples.extend(another_list_of_tuples)
print(list_of_tuples)
another_list_of_tuples.append((14, 15))
print(another_list_of_tuples)
