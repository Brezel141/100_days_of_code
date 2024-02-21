# Guess the number

import random
from replit import clear


def set_difficulty(difficulty):
        """Sets the difficulty of the game. Easy or Hard."""
        if difficulty == 'easy':
            return 10
        else: 
            return 5


def play_game(lives):
    """Main game function. User makes a guess and the game checks if the guess is correct."""
    playing = True
    while playing:
        print(f"You have {lives} Gusses remaining!")
        user_guess = int(input("Make a guess: "))

        if user_guess == random_number:
            print('You win!')
            playing = False
        elif user_guess < random_number:
            lives -= 1 
            print(f"Number too low.")
        elif user_guess > random_number:
            lives -= 1
            print(f"Number too high.")
        
        if lives == 0:
            print(f"No more guesses. The number was {random_number}")
            playing = False


again = False
while not again:
    print("welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    random_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or ' hard': ")
    lives = set_difficulty(difficulty)

    play_game(lives)    

    next_round = input("Play again? 'y' or 'n': ")
    if next_round == 'n':
        print("Bye bye")
        again = True
    else:
        clear()   