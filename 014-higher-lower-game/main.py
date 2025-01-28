import art
import game_data
import random


def refresh_screen():
    print(100 * "\n")
    print(art.logo)


def print_person_data(prefix, person):
    name = person["name"]
    description = person["description"]
    country = person["country"]
    print(f"{prefix}: {name}, a {description}, from {country}.")


def select_different_person(person_a):
    person_b = random.choice(game_data.data)

    while person_b["name"] == person_a["name"]:
        person_b = random.choice(game_data.data)

    return person_b


is_game_over = False
score = 0
person_a = random.choice(game_data.data)
refresh_screen()

while not is_game_over:
    person_b = select_different_person(person_a)
    print_person_data("Compare A", person_a)
    print(art.vs)
    print_person_data("Against B", person_b)

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_person_a_higher_than_person_b = (
        person_a["follower_count"] > person_b["follower_count"]
    )
    is_player_correct = (is_person_a_higher_than_person_b and guess == "a") or (
        not is_person_a_higher_than_person_b and guess == "b"
    )
    refresh_screen()

    if is_player_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        person_a = person_b
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True
