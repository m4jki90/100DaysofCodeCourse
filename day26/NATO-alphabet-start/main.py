import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in data.iterrows()}
word = input("Enter a word: ").upper()
alphabet = [dict[letter] for letter in word]
print(alphabet)