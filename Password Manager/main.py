from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    chars = [random.choice(letters) for x in range(random.randint(8, 10))]
    symbol = [random.choice(symbols) for x in range(random.randint(2, 4))]
    number = [random.choice(numbers) for x in range(random.randint(2, 4))]

    password_list = chars+symbol+number
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok and len(website)>0 and len(password)>0:
            with open("data.txt","a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
icon = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=icon)
canvas.grid(column=1,row=0)

text1 = Label(text="Website:")
text1.grid(column=0,row=1)

text2=Label(text="Email/Username:")
text2.grid(column=0,row=2)

text3=Label(text="Password:")
text3.grid(column=0,row=3)

website_entry = Entry(width=50)
website_entry.grid(column=1,row=1,columnspan=2)

email_entry = Entry(width=50)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"michal@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1,row=3)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=42, command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()