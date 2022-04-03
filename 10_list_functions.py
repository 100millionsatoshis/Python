numbers = [12, 98, 23, 87, 34, 76, 45, 65]
lucky_numbers = [77, 88]
participants = ["Michael", "Jim", "Dwight", "Pam", "Oscar", "Anjela", "Kevin"]
print(numbers)
print(lucky_numbers)
print(participants)
print("Now we join two lists together")
numbers.extend(lucky_numbers)
print(numbers)
print("This is another example of joining two lists")
participants.extend(lucky_numbers)
print(participants)
print("Now we add another item at the end of the list")
participants.append("Creed")
print(participants)
print("Now we insert item in the middle of the list")
participants.insert(3, "Kelly")
print(participants)
print("Now we remove items from list")
participants.remove(77)
print(participants)
print("Now we clear the list")
participants.clear()
print(participants)
print("And now, we add items back to the list")
participants = ["Michael", "Jim", "Dwight", "Pam", "Oscar"]
print(participants)
print("now we \"pop\" the last item from the list")
participants.pop()
print(participants)
print("Now we going to check an index number of a particular item in the list")
print(participants.index("Dwight"))
print("Now we add similar items to the list and check how many of them in the list")
participants.append("Jim")
print(participants.count("Jim"))
print("Now we sort the list")
participants.sort()
print(participants)
print("We can also reverse the order of the items in the list")
participants.reverse()
print(participants)
numbers.reverse()
print(numbers)
print("now we copy a list")
lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers2)
# The item at a certain index in a list can be reassigned.
numbers[2] = 66
print(numbers)
# It is possible to replace an item with an item of a different type.
numbers[3] = "tractor"
print(numbers)
# Lists can be added and multiplied and multiplied in the same way as strings.
print(participants + numbers * 2)
# To check if an item in a list, the in operator can be used. It returns True if the item occurs one or more times
# in the list, and False if it doesn't.
print("Jim" in participants)
# to check if an item is not in a list, you can use the not operator.
print("Pamela" not in participants)
print("Jim" not in participants)
# to get the number of items in a list we use len function.
print(len(participants))
# Unlike the index of the items, len does not start with 0.
print("Show participant list item with maximum value: " + str(max(participants)))
print("Show lucky_number list item with minimum value: " + str(min(lucky_numbers)))
