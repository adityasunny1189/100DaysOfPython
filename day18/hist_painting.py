import random
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.penup()
screen.colormode(255)
tim.speed("fastest")
tim.hideturtle()

def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = (r, g, b)
	return color

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for i in range(1, 101):
	tim.dot(20, random_color())
	tim.forward(50)

	if i % 10 == 0:
		tim.setheading(90)
		tim.forward(50)
		tim.setheading(180)
		tim.forward(500)
		tim.setheading(0)

screen.exitonclick()