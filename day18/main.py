from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("grey")

color_list = ["red", "blue", "green", "black", "yellow", "orange", "coral"]

for i in range(3, 11):
	tim.pencolor(color_list[random.randint(0, len(color_list) - 1)])
	tim.fillcolor(color_list[random.randint(0, len(color_list) - 1)])
	for j in range(i):
		tim.forward(100)
		tim.left(360/i)




screen = Screen()
screen.exitonclick()