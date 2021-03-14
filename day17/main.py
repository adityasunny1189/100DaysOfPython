from question_data import question_data
from question_class import question
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
	question_text = q["question"]
	question_ans = q["correct_answer"]
	new_question = question(question_text, question_ans)
	question_bank.append(new_question)

quiz = QuizBrain(question_bank) 

while quiz.still_has_questions():
	quiz.next_question()