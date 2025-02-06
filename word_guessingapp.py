import random

name = input("What is your name? ")
print("Good Luck!", name)

# List of words to choose from
words = ['MCA', 'MBA', 'BBA', 'BCOM']
word = random.choice(words)  # Choose a random word from the list

print("Guess the characters!")

guesses = ''  # To store guessed letters
turns = 5  # Number of allowed incorrect guesses

while turns > 0:
    failed = 0  # Counter for missing letters
    
    for char in word:
        if char in guesses:
            print(char, end=" ")  # Reveal guessed characters
        else:
            print("_")  # Hide unguessed characters
            failed += 1

    print()  # Move to a new line

    # If no failed attempts, the player has guessed the word
    if failed == 0:
        print("You win!")
        print("The word is:", word)
        break

    # Taking a character as input
    guess = input("Guess a character: ").upper()

    # Add guessed character to guesses
    guesses += guess  

    # Check if guessed character is incorrect
    if guess not in word:
        turns -= 1
        print("Wrong guess!")
        print("You have", turns, "more guesses left.")

        if turns == 0:
            print("You lose! The correct word was:", word)
