import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
pic = "blank_states_img.gif"
screen.addshape(pic)
turtle.shape(pic)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:

    answer = screen.textinput(f"{len(guessed_states)}/50 States Correct", "Type another state name: ").title()
    if answer == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        print(missed_states)

        break

    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)






