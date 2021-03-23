import turtle
import pandas

screen = turtle.Screen()
screen.setup(height = 500, width = 750)
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) 
turtle.penup()
turtle.tracer(0)
game_not_over = True 

# Get states name file
states = pandas.read_csv("50_states.csv")
states_name = states.state.to_list()
states_count = 0


while game_not_over:
	answer_imput = screen.textinput(title = f"{states_count}/{len(states.state)} the state", prompt = "what's another state name")
	if answer_imput in states_name:
		states_count += 1
		x_cor = states[states.state == answer_imput].x.to_list()[0]
		y_cor = states[states.state == answer_imput].y.to_list()[0]
		turtle.goto(x_cor, y_cor)
		turtle.write(answer_imput)

screen.exitonclick()