import random

print(
    """ _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/"""
)

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']
word_list = ["aardvark", "baboon", "camel"]
is_game_over = False
player_lives = 6
chosen_word = random.choice(word_list)
guessed_chars = []
word_length = len(chosen_word)

for _ in range(word_length):
    guessed_chars.append("_")
        
while not is_game_over:
    print(f"Word to guess: ", "".join(guessed_chars))
    
    has_guessed_letter_correctly = False
    guess = input("Guess a letter: ").lower()
    
    for i in range(word_length):
        chosen_word_letter = chosen_word[i]
        
        if guess == chosen_word_letter and guessed_chars[i] == "_":
            guessed_chars[i] = chosen_word_letter
            has_guessed_letter_correctly = True
            
        
    if not has_guessed_letter_correctly:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        player_lives -= 1
    else:
        print("".join(guessed_chars))
        
    if player_lives == 0:
        print(stages[0])
        print(f"***********************YOU LOSE**********************")
        is_game_over = True
        
    if "_" not in guessed_chars:
        print("****************************YOU WIN****************************")
        is_game_over = True
        
    if not is_game_over:
        print(stages[player_lives])
        print(f"****************************{player_lives}/6 LIVES LEFT****************************")