import turtle
import pandas
from names import Names
import os

screen = turtle.Screen()
screen.title("US STATES GAME")
screen.addshape("blank_states_img.gif")
if os.path.exists("listtolearn.csv"):
    os.remove("listtolearn.csv")

turtle.shape("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
correct = []

while len(correct) < 49:
    answer = screen.textinput(title=f"{len(correct)}/50 Correct", prompt="Give me another state name")
    answer = answer.title()
    if answer == "Exit":
        break
    if answer in data["state"].values:
        correct.append(answer)
        state_data = data[data["state"] == answer]
        x = state_data["x"].values[0]
        y = state_data["y"].values[0]
        name = Names(x,y, answer)

print(f"Congrats! You got {len(correct)} correct answers!")
print(f"Here are they: {correct}")
states_to_learn = [n for n in data["state"] if n not in correct]
print(states_to_learn)
df = pandas.DataFrame(states_to_learn)
df.to_csv("listtolearn.csv")