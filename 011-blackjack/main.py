import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


def initialize_player():
    player_stats = {
        "cards": [],
        "score": 0,
    }

    draw_card(player_stats)
    draw_card(player_stats)

    return player_stats


def draw_card(stats):
    card = random.choice(cards)
    stats["cards"].append(card)

    if stats["score"] + card > 21 and card == 11:
        stats["score"] += 1
    else:
        stats["score"] += card


def print_stats():
    print(f"\tYour cards: {user_stats["cards"]}, current score: {user_stats["score"]}")
    print(f"\tComputer's first card: {computer_stats["cards"][0]}")


while user_input.lower() == "y":
    user_stats = initialize_player()
    computer_stats = initialize_player()

    print(100 * "\n")
    print(art.logo)
    print_stats()

    if user_stats["score"] < 21:
        user_input = input("Type 'y' to get another card, type 'n' to pass: ")

    while user_input.lower() != "n" and user_stats["score"] < 21:
        draw_card(user_stats)
        print_stats()

        if user_stats["score"] < 21:
            user_input = input("Type 'y' to get another card, type 'n' to pass: ")

    if user_stats["score"] < 21:
        while computer_stats["score"] < user_stats["score"]:
            draw_card(computer_stats)

    print(
        f"\tYour final hand: {user_stats["cards"]}, final score: {user_stats["score"]}"
    )
    print(
        f"\tComputer's final hand: {computer_stats["cards"]}, final score: {computer_stats["score"]}"
    )

    if user_stats["score"] > 21:
        print("You went over. You lose 😭")
    elif computer_stats["score"] > 21:
        print("Opponent went over. You win 😁")
    elif user_stats["score"] > computer_stats["score"]:
        print("You win 😃")
    elif computer_stats["score"] > user_stats["score"]:
        print("You lose 😤")
    elif user_stats["score"] == computer_stats["score"]:
        print("Draw 🙃")

    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
