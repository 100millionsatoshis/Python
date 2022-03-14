secret_word = "Book"
guess = ""
while guess != secret_word:
    guess = input("Type your answer: ")
print("Correct!")

# This guessing game can be improved by setting limit on the number of user input

secret_word = "banana"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Type your answer: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You have already used three attempts. Gave over!")
else:
    print("Correct!")
