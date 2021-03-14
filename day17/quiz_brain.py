class QuizBrain:
	def __init__(self, question_list):
		self.question_number = 0
		self.score = 0
		self.gameover = False
		self.question_list = question_list

	def still_has_questions(self):
		if self.question_number == len(self.question_list) or self.gameover:
			return False
		return True

	def next_question(self):
		current_question = self.question_list[self.question_number]
		self.question_number += 1
		user_ans = input(f"Q {self.question_number}. {current_question.question}: ")
		self.check_answer(user_ans, current_question.ans)

	def check_answer(self, u_ans, c_ans):
		if u_ans == c_ans:
			self.score += 1
			print("You got it right")
		else:
			self.gameover = True
			print("You got it wrong")
		print(f"Your current score is {self.score}/{self.question_number}")