import art


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


print(art.logo)

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

user_input = "n"
first_number = 0
second_number = 0

while True:
    if user_input == "n":
        print("\n" * 100)
        print(art.logo)
        first_number = float(input("What's the first number?: "))

    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    result = operations[operation](first_number, second_number)

    user_input = input(
        f"Type 'y' top continue calculating with {result}, or type 'n' to start a new calculation: "
    )

    if user_input == "y":
        first_number = result
