from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(bg=THEME_COLOR, padx=50, pady=10)

        self.score_label = Label(text=f"score = {self.quiz.score}", font=('Arial', 18, 'bold'))
        self.score_label.config(bg=THEME_COLOR, pady=10, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=300, width=300, bg='white')
        self.question = self.canvas.create_text(150, 150, width=280, fill=THEME_COLOR, text='Questions', font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_button_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=self.true_button_image, command=self.check_ans_true)
        self.true_button.grid(row=2, column=0)

        self.false_button_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_button_image, command=self.check_ans_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text='Quiz Over')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def check_ans_true(self):
        ans = self.quiz.check_answer('True')
        self.give_feedback(ans)

    def check_ans_false(self):
        ans = self.quiz.check_answer('False')
        self.give_feedback(ans)

    def give_feedback(self, ans):
        if ans:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
