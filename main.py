import random
from check_word import check_word
from words import words
import display
import os

max_turns = 2
chosen_word = random.choice(words)

# Create empty game status word for display
game_status = []
for n in range(len(chosen_word)):
    game_status += "_"

print(chosen_word)
# Begin game loop
turn_count = 0
game_on = True
while game_on:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Let's Play Hangman!\n")
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
        turn_count += 1
        input(f"There are NOT any {guess}'s.")

    # Check for end game scenario
    if not "_" in game_status:
        print("You win!")
        game_on = False
    elif turn_count >= max_turns:
        print("Too bad! You lose!")
        game_on = False

print("Thanks for playing hangman!")