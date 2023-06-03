from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterFace():

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)
        self.score = 0
        self.question_num = 0
        self.score_label = Label(self.window,text=f"Score: {self.score}",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(self.window,width=300,height=250)

        self.question_text = self.canvas.create_text((150,125)
                                                     ,text="Some question text"
                                                     ,fill=THEME_COLOR,
                                                     width=270,
                                                     font=("ariel",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,padx=50,pady=50)
        self.right_im = PhotoImage(file="images/true.png")
        self.wrong_im = PhotoImage(file="images/false.png")
        self.right_bt =Button(self.window,image=self.right_im,padx=20,command=lambda :self.check_answer("True"))
        self.right_bt.grid(row=2,column=0,padx=20)
        self.wrong_bt = Button(self.window,image=self.wrong_im,padx=20,command=lambda :self.check_answer("False"))
        self.wrong_bt.grid(row=2,column=1,padx=20)
        self.next_question()
        self.window.mainloop()


    def next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions() :
            self.wrong_bt.config(state=NORMAL)
            self.right_bt.config(state=NORMAL)
            self.question_num += 1
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=question)

        else:
            self.canvas.itemconfig(self.question_text, text="You've reached ths end of the quiz")
            self.wrong_bt.config(state=DISABLED)
            self.right_bt.config(state=DISABLED)


    def check_answer(self,answer):
        self.wrong_bt.config(state=DISABLED)
        self.right_bt.config(state=DISABLED)
        self.get_feedback(self.quiz.check_answer(answer))


    def uplode_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.window.update()


    def get_feedback(self,check_answer):
        if check_answer:
            self.uplode_score()
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.next_question)