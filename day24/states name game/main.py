import turtle
import pandas

screen = turtle.Screen()
screen.setup(height = 500, width = 750)
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get states name file
states = pandas.read_csv("50_states.csv")
states_name = states.state.to_list()
states_count = 0
gussed_state = []

while states_count < 50:
	answer_imput = screen.textinput(title = f"{states_count}/{len(states.state)} the state", prompt = "what's another state name").title()
	if answer_imput == "Exit":
		break

	if answer_imput in states_name:
		states_count += 1
		gussed_state.append(answer_imput)
		state_data = states[states.state == answer_imput]
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		t.goto(int(state_data.x), int(state_data.y))
		t.write(answer_imput)


# Store the left over state in a csv file
left_states = [s for s in states_name if s not in gussed_state]
states_not_guessed = pandas.DataFrame(left_states)
states_not_guessed.to_csv("states_not_guessed.csv")
