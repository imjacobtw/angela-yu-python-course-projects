print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill_with_tax = total_bill * (1 + (tip_percentage / 100))
price_per_person = round(total_bill_with_tax / people, 2)

print(f"Each person should pay: ${price_per_person}")