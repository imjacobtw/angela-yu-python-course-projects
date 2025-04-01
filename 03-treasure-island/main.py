print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-\"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************""")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
user_input = input("\tType \"left\" or \"right\"\n")

if user_input == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    user_input = input("\tType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    
    if user_input == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        user_input = input("\tOne red, one yellow, and one blue. Which color do you choose?\n")
        
        if user_input == "red":
            print("You were burned by fire. Game Over!")
        elif user_input == "yellow":
            print("You found the treasure! You won!")
        elif user_input == "blue":
            print("You were eaten by beasts. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You were attacked by a trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")