from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
FONT_NAME = "Arial"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        # Disable the resizable property
        self.window.resizable(False, False)

        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Load logo image
        logo_image = PhotoImage(file="quiz/images/logo.png")
        self.logo_label = Label(image=logo_image, bg=THEME_COLOR)
        self.logo_label.image = logo_image  # Keep a reference to prevent garbage collection
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=(FONT_NAME, 20, "bold"))
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg=WHITE, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=(FONT_NAME, 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="quiz/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed, bd=0, activebackground=WHITE)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file="quiz/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed, bd=0, activebackground=WHITE)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\n{self.quiz.score} / {len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)
