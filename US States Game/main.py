import turtle
import pandas

screen = turtle.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
guesses = []
data = pandas.read_csv("50_states.csv")
states = data.state.tolist()

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's the another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guesses:
                missing_states.append(state)
        missing = pandas.DataFrame(missing_states)
        missing.to_csv("learn.csv")
        break

    for state in states:
        if state == answer_state:
            if state not in guesses:
                state_data = data[data.state == state]
                score += 1
                guesses.append(state)
                x = turtle.Turtle()
                x.hideturtle()
                x.penup()
                x.goto(x=state_data.x.item(),y=state_data.y.item())
                x.write(state)
                

screen.exitonclick()






