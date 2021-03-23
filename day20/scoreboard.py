from turtle import Turtle 

class ScoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.highscore = 0
		with open("highscore.txt") as file:
			hs = file.read()
			self.highscore = int(float(hs))
		self.color("white")
		self.penup()
		self.goto(0, 270)
		self.hideturtle()
		self.update_score()

	def update_score(self):
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.highscore}", align = "center", font = ("Arial", 24, "normal"))

	def reset(self):
		if self.score > self.highscore:
			self.highscore = self.score
		with open("highscore.txt", mode = "w") as file:
			file.write(str(self.highscore))
		self.score = 0
		self.update_score()

	# def game_over(self):
		# self.goto(0, 0)
		# self.write("GAME OVER", align = "center", font = ("Arial", 25, "normal"))

	def increment(self):
		self.score += 1
		self.clear()
		self.update_score()