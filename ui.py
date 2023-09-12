from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"  # 064663


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # use type hints, so that file can interpret the code easily
        # here quiz_brain: QuizBrain , -> I'm saying that the parameter,quiz_brain is an object of class QuizBrain

        self.quiz = quiz_brain
        self.current_score = self.quiz.score

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=15, padx=30, bg=THEME_COLOR)

        # ----------------------
        self.score_label = Label(text=f"Score: {self.current_score}", fg="white",
                                 bg=THEME_COLOR, font=("Courier", 14, "normal"))
        self.score_label.grid(column=1, row=0, pady=15)
        # ----------------------------

        self.canvas = Canvas(width=350, height=300, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(175, 150, width=340, text="Some questions",
                                                     font=("Arial", 15, "italic"), fill=THEME_COLOR)
        # width: 340 -> means wrapping up the text from the original canvas width, i.e, 350s
        self.canvas.grid(column=0, columnspan=2, row=1, pady=36)
        # ----------------------

        self.right_img = PhotoImage(file="images/true.png")
        self.right = Button(image=self.right_img, bd=0, activebackground=THEME_COLOR, command=self.is_true)
        self.right.grid(column=0, row=2, pady=10)
        # ----------------------

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong = Button(image=self.wrong_img, bd=0, activebackground=THEME_COLOR, command=self.is_false)
        self.wrong.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        correct_answer = self.quiz.check_answer("False")
        self.give_feedback(correct_answer)

    def get_next_question(self):

        self.buttons_state("active")
        self.canvas["bg"] = "white"
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, fill="purple",
                                   text=f"You've completed the Quiz\n Your final "
                                        f"score is: {self.quiz.score}/{len(self.quiz.question_list)}")
            # can provide more ui by using if /else to show the emojis
            self.buttons_state("disabled")

    def give_feedback(self, answer):
        if answer:  # True
            self.canvas["bg"] = "green"
        else:  # False
            self.canvas["bg"] = "red"
        self.canvas.itemconfig(self.question_text, fill="white")  # also change the text color to white
        self.score_label["text"] = f"Score: {self.quiz.score}"  # update score

        self.buttons_state("disabled")

        self.window.after(1000, self.get_next_question)

    def buttons_state(self, state):
        self.right.config(state=state)
        self.wrong.config(state=state)

