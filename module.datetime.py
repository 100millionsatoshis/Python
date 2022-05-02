# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as
# date objects.
# Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)

# Return the year and name of weekday:
print(x.year)
print(x.strftime("%A"))

# I should continue this topic once I practice object and class module.
