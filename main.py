import random
from check_word import check_word
from words import words
import display, hangman_art
import os

max_turns = 2
chosen_word = random.choice(words)

# Create empty game status word for display
game_status = []
for n in range(len(chosen_word)):
    game_status += "_"

print(hangman_art.logo + "\n")
input("Let's Play Hangman!\n")

# Begin game loop
remaining_attempts = 7
game_on = True
while game_on:
    # Clear console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display game status
    print(hangman_art.stages[remaining_attempts - 1])
    display.display_game_status(game_status)
    print("\n")

    # Get user guess
    guess = input("Guess a letter: ").lower()


    # Check word for occurrances of user guess
    indexes = check_word(guess, chosen_word)
    count_correct = len(indexes)
    if guess in game_status:
        input("You already guessed that!")
    elif count_correct > 0:
        input(f"There are {count_correct} {guess}'s!")
        for index in indexes:
            game_status[index] = guess
    else:
        remaining_attempts -= 1
        input(f"There are NOT any {guess}'s.")

    # Check for end game scenario
    if not "_" in game_status:
        print("You win!")
        game_on = False
    elif  remaining_attempts <= 0:
        print("Too bad! You lose!")
        game_on = False

print("Thanks for playing hangman!")