from turtle import Turtle

POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		for position in POSITIONS:
			self.add_segment(position)

	def add_segment(self, position):
		segment = Turtle("square")
		segment.color("red")
		segment.penup()
		segment.goto(position)
		self.segments.append(segment)

	def extend(self):
		self.add_segment(self.segments[-1].position())

	def reset(self):
		for seg in self.segments:
			seg.goto(1000, 1000)
		self.segments.clear()
		self.create_snake()
		self.head = self.segments[0]

	def move(self):
		for seg_num in range(len(self.segments) - 1, 0, -1):
			x_cor = self.segments[seg_num - 1].xcor()
			y_cor = self.segments[seg_num - 1].ycor()
			self.segments[seg_num].goto(x_cor, y_cor)
		self.segments[0].forward(MOVE_STEP)

	def up(self):
		if self.segments[0].heading() != DOWN:
			self.segments[0].setheading(UP)

	def down(self):
		if self.segments[0].heading() != UP:
			self.segments[0].setheading(DOWN)

	def left(self):
		if self.segments[0].heading() != RIGHT:
			self.segments[0].setheading(LEFT)

	def right(self):
		if self.segments[0].heading() != LEFT:
			self.segments[0].setheading(RIGHT)
