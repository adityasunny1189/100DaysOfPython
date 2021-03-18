from turtle import Turtle, Screen
import requests as req
import json

tim = Turtle()
screen = Screen()

tim.penup()
tim.hideturtle()
screen.setup(height = 800, width = 800)
tim.goto(0, 370)
tim.setheading(270)

response = req.get('https://dog.ceo/api/breeds/list/all')
json_data = response.text
python_data = json.loads(json_data)
hound_breeds = python_data['message']['hound']
poodle_breeds = python_data['message']['poodle']
print(f"Poodle Breeds Count: {len(poodle_breeds)}")
for i in hound_breeds:
	tim.write(i, font = ('Arial', 18, 'normal'))
	tim.forward(100)

screen.exitonclick()