import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="What's another state?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        loc = data[data["state"] == answer_state]
        t.goto(float(loc.x.item()), float(loc.y.item()))
        t.write(answer_state)

missed_states = list(set(all_states) - set(guessed_states))

print("Missed the following States:")
for state in missed_states:
    print(state)

