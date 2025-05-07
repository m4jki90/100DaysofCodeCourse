from tkinter import *
FONT = ("Arial", 16, "bold")

def calculate():
    value = float(input.get()) * 1.60
    km_value.config(text=int(value))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20,pady=20)

input = Entry(width=10)
input.grid(column=1,row=0)


text1 = Label(text="Miles", font = FONT)
text1.grid(column=2,row=0)
text1.config(padx=20)

text2 = Label(text="is equal to ", font=FONT)
text2.grid(column=0,row=1)

km_value = Label(text="",font=FONT)
km_value.config(text="",padx=10,pady=10)
km_value.grid(column=1,row=1)


text3=Label(text="Km",font=FONT)
text3.grid(column=2,row=1)

button = Button(text="Calculate",command = calculate)
button.grid(column=1,row=2)

window.mainloop()

