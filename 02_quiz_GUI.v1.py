from tkinter import *
from functools import partial   # To prevent unwanted windows
import random

class Start:
    def __init__(self, parent):

        # GUI to select number of question, range of numbers and a level
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.press_button = Button(text="Press", command=self.to_play)
        self.press_button.grid(row=0, pady=10)

    def to_play(self):

        # retrieve selected questions
        selected_questions = 30
        levels = 1

        Quiz(self, levels, selected_questions)

        # hide start up window
        root.withdraw()


class Quiz:
    def __init__(self, partner, levels, selected_questions):
        print(levels)
        print(selected_questions)

        # initialise variables
        self.questions = IntVar()
        
        # Set number of questions to amount entered by users at start of quiz
        self.questions.set(selected_questions)
        
        # GUI setup
        self.quiz_box = Toplevel()
        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        # Mode row 0
        self.Mode_label = Label(self.quiz_frame, text="Quiz",
                                font="Arial 24 bold", padx=10,
                                pady=10)
        self.Mode_label.grid(row=0)

        # Heading row 1
        self.heading_label = Label(self.quiz_frame, text=" Please, enter an answer in the white space below  and"
                                                         " then click the 'Submit' button to proceed with your answer."                                                                            
                                                         " To move on to the next question click the 'Next' button.",
                                   font="Arial 10", padx=10, wrap=400,
                                   pady=10)
        self.heading_label.grid(row=1)

        # Questions Box (row 2)
        self.questions_box = Label(self.quiz_frame, bg="#FFCCFF",
                                   font="Arial 22 bold", width=10,
                                   padx=10, pady=10)
        self.questions_box.grid(row=2)

        # answers entry box (row 3)
        self.answers_entry_frame = Frame(self.quiz_frame, width=200)
        self.answers_entry_frame.grid(row=3)

        self.answers_entry = Entry(self.answers_entry_frame,
                                        font="Arial 28 bold", width=10)
        self.answers_entry.grid(row=0)

        self.submit_button = Button(self.answers_entry_frame,
                                       font="Arial 14 bold",
                                       text="Submit", bg="#FFFF33", width=10)
        self.submit_button.grid(row=1, column=0)

        self.next_button = Button(self.answers_entry_frame,
                                       font="Arial 14 bold", width=10,
                                       text="Next→", bg="#00CC00", fg="white")
        self.next_button.grid(row=1, column=1)

        self.answers_error_label = Label(self.answers_entry_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.answers_error_label.grid(row=4, columnspan=2, pady=10)

        # Error Label goes here
        self.answers_error_label = Label(self.quiz_frame, fg="red", font="Arial 14 italic",
                                        text="", justify=CENTER)
        self.answers_error_label.grid(row=4)



        # selected questions Label (row 4)

        self.questions_label = Label(self.quiz_frame, text="Welcome, your selected number of questions: 30 ", font="Arial 12 bold",
                                   fg="green", wrap=300, justify=LEFT)
        self.questions_label.grid(row=4, pady=10)

        # Help/Rules and quiz results button (row 5)
        self.help_export_frame = Frame(self.quiz_frame)
        self.help_export_frame.grid(row=5)

        self.help_button = Button(self.help_export_frame, text="How to Play?",
                                  font="Arial 15 bold", bg="#808080", fg="white")
        self.help_button.grid(row=5, column=0, padx=2, pady=10)

        self.results_button = Button(self.help_export_frame, text="Quiz Results...",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.results_button.grid(row=5, column=1, padx=2, pady=10)

    def reveal_boxes(self):

        # retrieve the questions from the initial function..
        current_questions = self.questions.get()

        # adjust the questions (subtract quiz cost and add pay out)
        # For testing purposes, just add 2
        current_questions +=2

        # Set questions to adjust questions
        self.questions.set(current_questions)

        # Edit label so user can see their questions
        self.questions_label.configure(text="questions: {}".format(current_questions))
        


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start(root)
    root.mainloop()
