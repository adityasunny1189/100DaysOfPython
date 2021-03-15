from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(15)
color_list = ["red", "blue", "green", "black", "yellow", "orange", "coral"]

direction = [0, 90, 180, 270]
def random_walk(dis):
	tim.pencolor(color_list[random.randint(0, len(color_list) - 1)])
	tim.forward(50)
	tim.setheading(dis)

for i in range(100):
	d = direction[random.randint(0, len(direction) - 1)]
	random_walk(d)

screen = Screen()
screen.exitonclick()