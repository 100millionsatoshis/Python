# dictionary is a special structure in python which allows us store information what are called key value pair

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Okt": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversions["Nov"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Luv"))
# default value
print(monthConversions.get("Tom", "Not valid key"))

# key can be a number

customerID = {
    "001": "Ken Adams",
    "002": "Ethan Chase",
    "003": "Michael Saylor",
}

print(customerID.get("002"))

# each key has to be unique
