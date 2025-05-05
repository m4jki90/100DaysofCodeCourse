#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("Input/Names/invited_names.txt") as f:
    names = f.readlines()
    
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for x in names:
        name = x.strip()
        final_letter = letter.replace("[name]", str(name))
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as personal_letter:
            personal_letter.write(final_letter)

