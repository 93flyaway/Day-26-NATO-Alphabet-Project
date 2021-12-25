import pandas

nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}

user_word = input("Enter a word: ").upper()
result = [nato_alphabet_dict[char] for char in user_word]

print(result)
