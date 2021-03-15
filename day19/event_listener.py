from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.listen()

def move_forward():
	tim.forward(10)

def move_backward():
	tim.backward(10)

def turn_right():
	new_heading = tim.heading() + 10
	tim.setheading(new_heading)

def turn_left():
	new_heading = tim.heading() - 10
	tim.setheading(new_heading)

def reset_screen():
	screen.reset()

screen.onkey(key="a", fun=move_forward)
screen.onkey(key="d", fun=move_backward)
screen.onkey(key="w", fun=turn_right)
screen.onkey(key="s", fun=turn_left)
screen.onkey(key="c", fun=reset_screen)

screen.exitonclick()