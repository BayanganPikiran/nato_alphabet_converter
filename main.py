import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


user_name = input("Please type your name:\n").upper()
nato_name = [nato_dict[char] for char in user_name if char != " "]

print(f"Your name using the NATO alphabet is: {nato_name}")





# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

