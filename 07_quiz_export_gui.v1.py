from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Quiz:
    def __init__(self):
        # Formatting variables...
        self.quiz_results_list = [10, 30]

        # In actual program this is blank and is populated with user calculation
        self.round_results_list = []

        self.quiz_frame = Frame()
        self.quiz_frame.grid()

        # Heading Row
        self.heading_label = Label(self.quiz_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # History Button (row 1)
        self.results_button = Button(self.quiz_frame, text="Quiz Results",
                                   font="Arial 14",
                                   padx=10, pady=10,
                                   command=lambda: self.to_results(self.round_results_list, self.quiz_results_list))
        self.results_button.grid(row=1)

        if len(self.round_results_list) == 0:
            self.results_button.config(state=NORMAL)

    def to_results(self, quiz_history, quiz_results):
        QuizResults(self, quiz_history, quiz_results)


class QuizResults:
    def __init__(self, partner, quiz_history, quiz_results):

        print(quiz_history)

        # disable help button
        partner.results_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (i.e: history box)
        self.results_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.results_box.protocol('WM_DELETE_WINDOW', partial(self.close_results, partner))

        # Set up GUI Frame
        self.results_frame = Frame(self.results_box)
        self.results_frame.grid()

        # Set up help heading (row 0)
        self.results_heading = Label(self.results_frame,text="Quiz Results",
                                 font="arial 19 bold")
        self.results_heading.grid(row=0)

        # To Export <instruction>  (row 1)
        self.export_instructions = Label(self.results_frame,
                                         text="Here are your quiz results "
                                              "Please use the "
                                              "Export button to access the results "
                                              "of each round that you played ",
                                         wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, width=40, fg="green",
                                         padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Selected Questions (row 2)
        self.details_frame = Frame(self.results_frame)
        self.details_frame.grid(row=2)

        # Score (row 2.0)
        self.score_label = Label(self.details_frame, font=heading, text="Score: {}/{}"
                                 .format(quiz_results[0], quiz_results[1]))
        self.score_label.grid(row=0, column=0, padx=0)

        # Correct answers (row 2.1)
        self.correct_ans_label = Label(self.details_frame, font=heading,
                                       text="Correct Answers: {}"
                                       .format(quiz_results[0]))
        self.correct_ans_label.grid(row=1, column=0, padx=0)

        # Wrong Answers (row 2.2)
        self.wrong_ans_label = Label(self.details_frame, font=heading,
                                     text="Wrong Answers: {}"
                                     .format(quiz_results[1]-quiz_results[0]))
        self.wrong_ans_label.grid(row=3)

        # Percentage (row 2.3)
        self.percentage_label = Label(self.details_frame, font=heading,
                                      text="Percentage: {:.1f}%".format(quiz_results[0]/quiz_results[1]*100))
        self.percentage_label.grid(row=4)

        # Dismiss button (row 3)
        self.dismiss_button = Button(self.details_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     width=10, bg="#660000", fg="white",
                                     command=partial(self.close_results, partner))
        self.dismiss_button.grid(row=5, column=0, pady=10)

    def close_results(self, partner):
        # Put stats back to normal...
        partner.results_button.config(state=NORMAL)
        self.results_box.destroy()


# main routine:
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    something = Quiz()
    root.mainloop()
