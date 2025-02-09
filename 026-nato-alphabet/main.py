import pandas

nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for index, row in nato_alphabet_df.iterrows()}

user_input = input("Enter a word: ").upper()

phonetic_code_words = [nato_alphabet[letter] for letter in user_input]
print(phonetic_code_words)
