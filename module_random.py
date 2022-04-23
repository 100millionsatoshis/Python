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
