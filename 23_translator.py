# let's imagine we have an imaginary language, in which, all the vowels are equal to "g"


def translate(word):
    translation = ""
    for letter in word:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a word: ")))

# in this example we are using "for loop" in combination with "if loop".
# now we improve this program a little.
# program above ignores uppercase letter and turns into lowercase "g"
# Now we are going to fix it in the program below by adding one more layer of "if" statement:


def translate(word):
    translation = ""
    for letter in word:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Now, let's run improved version. Enter a word: ")))
