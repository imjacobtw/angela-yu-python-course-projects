import random

GAME_RESULTS = ["It's a draw!", "You win!", "You lose!"]
ROCK_PAPER_SCISSORS_ASCII_ART = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print(ROCK_PAPER_SCISSORS_ASCII_ART[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(ROCK_PAPER_SCISSORS_ASCII_ART[computer_choice])

print(GAME_RESULTS[user_choice - computer_choice])
