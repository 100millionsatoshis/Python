# seed() Initialize the random number generator
import random
random.seed(11)
print(random.random())
# The seed() method is used to initialize the random number generator.
# The random number generator needs a number to start with (a seed value), to be able to generate a random number.
# By default, the random number generator uses the current system time.
# Use the seed() method to customize the start number of the random number generator.
# Note: If you use the same seed value twice you will get the same random number twice.

# getstate() Returns the current internal state of the random number generator
print(random.getstate())
# The getstate() method returns an object with the current state of the random number generator.
# Use this method to capture the state, and use the setstate() method, with the captured state, to restore the state

# setstate() Restores the internal state of the random number generator.
print(random)
state = random.getstate()
print(random.random())
random.setstate(state)
print(random.random())

# getrandbits() Returns a number representing the random bits.
print("This is an 8 bits sized integer:", random.getrandbits(8))
# returns an 8 bit sized integer

# randrange() Returns a random number between the given range
print("Return a number between 3 and 9:", random.randrange(3, 9))
# random.randrange(start, stop, step)
# start Optional. An integer specifying at which position to start.
# Default 0
# stop 	Required. An integer specifying at which position to end.
# step 	Optional. An integer specifying the incrementation.
# Default 1

# randint() Returns a random number between the given range.
print("Return a number between 3 and 9:", random.randint(3, 9))
# Note: This method is an alias for randrange(start, stop+1).
# syntax: random.randint(start, stop)
# start: Required. An integer specifying at which position to start.
# stop:	Required. An integer specifying at which position to end.

# choice() 	Returns a random element from the given sequence:
mylist = ["apple", "banana", "cherry"]
print("Return a random element from a list:", random.choice(mylist))
# The choice() method returns a randomly selected element from the specified sequence.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

# choices() Returns a list with a random selection from the given sequence:
print("Return a list with 14 items. The list should contain a randomly selection of the values from a specified \n "
      "list, and there should be 10 times higher possibility to select \"apple\" than the other two: \n",
      random.choices(mylist, weights=[3, 0, 1], k=14))

# The choices() method returns a list with the randomly selected element from the specified sequence.
# You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
# Syntax:
# random.choices(sequence, weights=None, cum_weights=None, k=1)
# sequence: Required. A sequence like a list, a tuple, a range of numbers etc.
# weights: Optional. A list were you can weigh the possibility for each value.
# Default: None
# cum_weights: Optional. A list were you can weigh the possibility for each value, only this time the possibility is
# accumulated.
# Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4].
# Default None
# k Optional. An integer defining the length of the returned list

# shuffle() Takes a sequence and returns the sequence in a random order:
breakfast_options = ["oatmeal", "sausage", "sandwich", "musli", "cheese", "pizza"]
random.shuffle(breakfast_options)
print(breakfast_options)
# The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
# Syntax:
# random.shuffle(sequence, function)
# sequence 	Required. A sequence.
# function 	Optional. The name of a function that returns a number between 0.0 and 1.0.
# If not specified, the function random() will be used


def special_shuffle():
    return 0.4


random.shuffle(breakfast_options, special_shuffle)
print(breakfast_options)
