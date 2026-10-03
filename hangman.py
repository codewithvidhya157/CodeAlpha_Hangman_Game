import random

# List of 5 predefined words
words = ["python", "computer", "coding", "program", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses
incorrect_guesses = 0
max_incorrect_guesses = 6

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while incorrect_guesses < max_incorrect_guesses:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

    # Display updated count
    print("Incorrect guesses:", incorrect_guesses, "/", max_incorrect_guesses)

else:
    print("\nGame Over!")
    print("The word was:", word)