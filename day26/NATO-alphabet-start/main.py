import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in data.iterrows()}
def generate():
    word = input("Enter a word: ").upper()
    try:
        alphabet = [dict[letter] for letter in word ]
    except KeyError:
        print("Sorry,only letters in the alphabet please.")
        generate()
    else:
        print(alphabet)

generate()