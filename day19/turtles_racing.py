from turtle import Turtle, Screen
import random

screen = Screen()

is_game_on = False

colors = ["red", "green", "blue", "coral", "orange", "violet", "yellow"]
screen.setup(height = 400, width = 500)
user_bet = screen.textinput(title = "Make your bet", prompt = "What is your bet: ")

turtles = []

distance = 0

for c in colors:
	t = Turtle(shape = "turtle")
	t.color(c)
	t.penup()
	t.goto(x = -225, y = -100 + distance)
	distance += 40
	turtles.append(t)

if user_bet:
	is_game_on = True

while is_game_on:
	for turtle in turtles:
		if turtle.xcor() >= 200:
			if user_bet != turtle.pencolor():
				print(f"{user_bet} lost, the winner is {turtle.pencolor()}")
			else:
				print("You win")
			is_game_on = False
		turtle.forward(random.randint(0, 10))


screen.exitonclick()