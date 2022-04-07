"""
The range function returns a sequence of numbers.
By default, it starts from 0, increments by 1 and stops before the specified number.
The code below generates a list containing all the integers up to 10.
"""
numbers = list(range(10))
print(numbers)

# In order to output the range as a list, we need to explicitly convert it to a list, using the list() function.
# If range is called with one argument, it produces objects with values from 0 to that argument.
# if it is called with 2 arguments, it produces values from first to the second.

nums = list(range(3, 8))
print(nums)
print(range(20) == range(0, 20))

# Remember the second argument is not included in the range, so range(3, 8) will not include the number 8.
# Range can have a third argument, which determines the interval of the sequence produced, also called step.

numbers = list(range(5, 20, 2))
print(numbers)

# We can create list of decreasing numbers, using a negative number as the third argument,
# for example list(range(20, 5, -2)

# For loops is commonly used to repeat some code a certain number of times. This is done by combining for loops with
# range objects.

for i in range(5):
    print("hello")
# You do not need to call list on the range object when it is used in a for loop, because it isn't being indexed,
# so a list isn't required. 
