from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Break",fg=PINK)
    else:
        countdown(work_sec)
        label.config(text="Work",fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if count % 60 == 0:
        canvas.itemconfig(timer_text,text=f"{minutes}:00")
    else:
        canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark = ""
        work_ses = math.floor(reps/2)
        for x in range(work_ses):
            mark+="✔"
        checkmark_button.config(text=mark)
           
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


label=Label(text="Timer",bg=YELLOW,font=(FONT_NAME,40,"bold"),fg=GREEN)
label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,125,text="00:00", fill="white", font=(FONT_NAME,25,"bold"))
canvas.grid(column=1,row=1)


start_button= Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,command=reset)
reset_button.grid(column=2,row=2)

checkmark_button=Button(fg=GREEN , bg=YELLOW)
checkmark_button.grid(column=1,row=3)


window.mainloop()
