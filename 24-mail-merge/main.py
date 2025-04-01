names = []

with open("./Input/Names/invited_names.txt") as names_file:
    for name_line in names_file.readlines():
        name = name_line.strip()
        names.append(name)

with open("./Input/Letters/starting_letter.txt") as letter_template_file:
    letter_template = letter_template_file.read()

    for name in names:
        letter = letter_template.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter_file:
            letter_file.write(letter)