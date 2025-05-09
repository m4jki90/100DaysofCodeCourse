from tkinter import *
import pandas 
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")

card = {}

def next():
    global card
    global timer
    window.after_cancel(timer)
    card = random.choice(data_dict)
    canvas.itemconfig(lang,text="French", fill="black")
    canvas.itemconfig(word,text=card["French"], fill="black")
    canvas.itemconfig(image,image=front)
    timer = window.after(3000,func=flip)
    
def flip():
    canvas.itemconfig(lang, text="English",fill="white")
    canvas.itemconfig(word, text = card["English"],fill="white")
    canvas.itemconfig(image, image=back)

def add():
    data_dict.remove(card)
    csv_data = pandas.DataFrame(data_dict)
    csv_data.to_csv("data/words_to_learn.csv", index=False)
    next()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip)

canvas = Canvas(width=800,height=526)
front = PhotoImage(file = "images/card_front.png")
back = PhotoImage(file = "images/card_back.png")
image = canvas.create_image(400,263,image = front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
lang =canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

wrong_image = PhotoImage(file = "images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next)
wrong_button.grid(column=0,row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=add)
right_button.grid(column=1,row=1)

next()

window.mainloop()