import random

def play_game():
    # Generate a random number between 1 and 100
    rand_num = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the guessing game! Guess a number between 1 and 100.")
    while guess != rand_num:
        guess = int(input("Enter your guess: "))
        if guess < rand_num:
            print("Too low! Guess again.")
        elif guess > rand_num:
            print("Too high! Guess again.")
        else:
            print("Congratulations! You guessed the number.")
            print("It took you " + str(attempts) + " attempts.")
    attempts+=1

play_game()
