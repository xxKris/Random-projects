import random

# The words to choose from
words = ["python", "programming", "language", "computer", "science"]

# Choose a random word
word = random.choice(words)

# Create a list of underscores the same length as the word
hidden_word = ["_"] * len(word)

# The number of incorrect guesses the player has made
incorrect_guesses = 0

# The letters that the player has guessed
guessed_letters = []

# The maximum number of incorrect guesses
max_incorrect_guesses = 6

# The main game loop
while "_" in hidden_word and incorrect_guesses < max_incorrect_guesses:
    # Print the current state of the hidden word
    print(" ".join(hidden_word))
    
    # Print the guessed letters
    print("Guessed letters:", ", ".join(guessed_letters))
    
    # Get the player's guess
    guess = input("Guess a letter: ").lower()
    
    # Check if the letter has been guessed before
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    guessed_letters.append(guess)
    
    # Check if the letter is in the word
    if guess in word:
        # Replace the underscores with the letter
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        # Increment the number of incorrect guesses
        incorrect_guesses += 1
        print("Incorrect. You have", max_incorrect_guesses - incorrect_guesses, "guesses left.")

# Check if the player won or lost
if "_" not in hidden_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Sorry, you lost. The word was", word)
