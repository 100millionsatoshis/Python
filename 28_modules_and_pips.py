# module is a python file that we can import into our current python file
# if we wrote a python file that has a bunch of useful functions and variables we could take it and import it
# to the file we are currently working on.
import random
import useful_tools
from math import pi, sqrt
print(useful_tools.roll_dice(10))
print("now another example")
for i in range(5):
    value = random.randint(1, 8)
    print(value)


# The code above uses the randint function defined in the random module tp print 5 random numbers in the range 1 to 8

print(random.choice("London is the capital of Great Britain"))
""" There is another kind of import that can be used if you only need certain functions from a module.
These take the form from module_name import var, and then var can be used as it were defined normally in your code. 
For example, to import only the pi constant from the math module. 
We can use comma separated list to import multiple objects. For example: 
from math import sqrt, pi 
We can also use comma to import multiple modules. For example
import math, random, sys
* imports all objects from a module. For example: from math import * 
This is generally discouraged, as it confuses variables in your code with variables in the external module.
To see all available functions in a module use help function For example: 
print(help("math")). 
You can import a module or object under a different name using the as keyword. This is mainly used when a module or 
object has a long or confusing name. 
from math import sqrt as square_root. 
There are three main types of modules in Python, those you write yourself, those you install from external sources, 
and those that are preinstalled with Python. 
Preinstalled modules are called standard library, and contains many useful modules, such as string, re, datetime, 
math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse, and sys. 

"""

print(pi)
print(sqrt(9))
print(help(str))
