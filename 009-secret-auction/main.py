import art

print(art.logo)
print("Welcome to the secret auction program.")
bids = {}
people_are_bidding = "yes"

while people_are_bidding == 'yes':
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    people_are_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    print("\n" * 100)

highest_bid_name = ""
highest_bid_value = 0

for name in bids:
    if bids[name] > highest_bid_value:
        highest_bid_name = name
        highest_bid_value = bids[name]

print(f"The winner is {highest_bid_name} with a bid of ${highest_bid_value}.")
