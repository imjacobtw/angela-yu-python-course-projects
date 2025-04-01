import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "hard":
    attempts = 5
else:
    attempts = 10

number = random.randint(1, 100)
is_game_running = True

while is_game_running:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess < number:
        print("Too low.")
        attempts -= 1
    elif guess > number:
        print("Too high.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number}.")
        is_game_running = False

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        is_game_running = False
    elif attempts != 0 and is_game_running == True:
        print("Guess again.")
