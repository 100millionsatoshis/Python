"""
Lists are used to store items. A list is created using square brackets with commas separating items.
"""
activities = ["museum", "movie", "swimming", "hiking", "bar", "restaurant"]
print("Do you want to go to museum with me " + activities[1])
print("I am going to " + activities[-2] + ". Do you want to join me?")
print("How about you and me go to " + str(activities[1:]))
print("Would you like to go to " + str(activities[2:4]) + ' with me?')
activities[4] = "sushi bar"
print(activities[4])
"""
Sometimes you need to create an empty list and populate it later during the program. For example, if you are creating 
a queue management program, the queue is going to be empty in the beginning and get populated with people data later. 
An empty list is created with an empty pair of square brackets.  
"""

empty_list = []
"""
# In some code samples you might see a comma after the last item in the list. It is not mandatory, but perfectly valid.
Typically, a list will contain items of a single item type, but it is also possible to include several different types. 
Lists also can be nested within other lists. 
"""
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])
