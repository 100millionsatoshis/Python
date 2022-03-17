# 2 dimensional lists

number_grid = [
    [1, 2, 3],
    ["a", "b", "c"],
    [12, 13, 14],
    [0]
]
# now lets see how we can access individual items from this 2 dimensional list.
print(number_grid[0][0])
print(number_grid[1][1])

# now we use "nested for loop" in order to print our all elements of the list.

for row in number_grid:
    print(row)

# this way we can print out all rows of the list.

for row in number_grid:
    for column in row:
        print(column)
