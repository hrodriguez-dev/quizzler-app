from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
#Creates the quiz interface
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        #Window setup
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.resizable(False, False)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.timer_id = None

        #Score Label
        self.score_label = Label(text=f"Score: {self.score}", fg="white",
                                 bg=THEME_COLOR, font=("Arial", 20))
        self.score_label.grid(row=0, column=1, sticky=E)

        #Text Box and label
        self.white_box = Canvas(width=300, height=250, bg="white")
        self.white_box_txt = self.white_box.create_text(150, 125,width=280, text = self.quiz.next_question(),
                                                        font=("Arial", 20, "italic"))
        self.white_box.grid(row=1, column=0, columnspan=2, pady=20)

        #True and False buttons
        self.true_png = PhotoImage(file="images/true.png")
        self.true_bt = Button(image=self.true_png, bd=0, highlightthickness=0, command=self.true_button)
        self.true_bt.grid(row=2, column=0, pady=20)
        self.false_png = PhotoImage(file="images/false.png")
        self.false_bt = Button(image=self.false_png, bd=0, highlightthickness=0, command=self.false_button)
        self.false_bt.grid(row=2, column=1,pady=20)

        self.window.mainloop()

    #Show next question
    def get_next_question(self):
        self.timer_id = None
        question_text = self.quiz.next_question()
        self.white_box.itemconfig(self.white_box_txt, text=question_text)

    #True Button
    def true_button(self):
        if self.timer_id is None: #Avoid running windows.after multiple times
            result = self.quiz.check_answer("True")
            self.white_box.itemconfig(self.white_box_txt, text=result)
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            if self.quiz.still_has_questions(): #Stop next_question when quiz is over
                self.timer_id = self.window.after(1000, self.get_next_question)
            else:
                self.white_box.itemconfig(self.white_box_txt, text=f"{result}\n\nYou've completed the quiz!")

    #False Button
    def false_button(self):
        if self.timer_id is None: #Avoid running windows.after multiple times
            result = self.quiz.check_answer("False")
            self.white_box.itemconfig(self.white_box_txt, text=result)
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            if self.quiz.still_has_questions(): #Stop next_question when quiz is over
                self.timer_id = self.window.after(1000, self.get_next_question)
            else:
                self.white_box.itemconfig(self.white_box_txt, text=f"{result}\n\nYou've completed the quiz!")