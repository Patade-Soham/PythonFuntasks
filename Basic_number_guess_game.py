import random


logo = """
===========================
  NUMBER GUESSING GAME
===========================
"""

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    numbers = list(range(1, 101))
    num_to_guess = random.choice(numbers)

    difficulty = input('Choose a difficulty level ("easy" or "hard"): ').lower()

    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5
    else:
        print("Invalid input. Defaulting to 'hard' mode.")
        lives = 5

    print(f"You have {lives} attempts to guess the number.")

    while lives > 0:
        guess = int(input("\nMake a guess: "))
        if guess == num_to_guess:
            print(f"Congratulations! You guessed the number {num_to_guess} correctly!")
            break
        elif guess > num_to_guess:
            print("Too high.")
        else:
            print("Too low.")

        lives -= 1
        if lives > 0:
            print(f"You have {lives} guesses left. Try again!")
        else:
            print(f"You've run out of guesses. The number was {num_to_guess}. Better luck next time!")

while True:
    play_game()
    replay = input("\nDo you want to play again? Type 'yes' or 'no': ").lower()
    if replay != 'yes':
        print("Thanks for playing! Goodbye!")
        break
