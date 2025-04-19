TEXT_TO_MORSE_CODE: dict[str, str] = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "/",
}

user_input: str = input("Enter the text you would like to convert to morse code: ")
user_input_original: str = user_input
user_input_morse_code: str = ""
user_input = user_input.strip().upper()

try:
    for char in user_input:
        morse_code_char: str = TEXT_TO_MORSE_CODE[char]
        user_input_morse_code += f"{morse_code_char} "

    print(f"Original Text: {user_input_original}")
    print(f"Morse Code Translation: {user_input_morse_code}")
except KeyError as err:
    print(f"ERROR: Character {err} could not be translated to Morse code.")
