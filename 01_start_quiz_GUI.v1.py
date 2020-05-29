from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __int__(self, parent):

        # GUI to select number of question, range of numbers and a level
        self.start_frame = Frame(padx=20, pady=20)
        self.start_frame.grid()

        # Set Initial questions to zero
        self.questions = IntVar()
        self.questions.set(0)

        # Set Initial Lowest to zero
        self.lowest = IntVar()
        self.lowest.set(0)

        # Set Initial Highest to zero
        self.highest = IntVar()
        self.highest.set(0)

        # Maths Quiz Heading (row 0)
        self.quiz_label = Label(self.start_frame, font="arial 20 bold",
                                text="Maths Quiz", wrap=225,
                                justify=LEFT)
        self.quiz_label.grid(row=0)

        # Initial Instruction (row 1)
        self.quiz_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Welcome, test your mathematical skills."
                                               " Before selecting a level, "
                                               "please enter the number of question between (5-30)"
                                               " you would like to have in your quiz."
                                               " Then please enter the range of numbers between 0-1000(easy mode),"
                                               " 0-100(medium mode) you would like to see in your quiz. "
                                               "please choose a range of at least 10 numbers. "
                                               "For (hard mode) the range is already set to 0-50.",
                                          wrap=225, justify=LEFT, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)


# main routine
if __name__ == "__main__":
   root = Tk()
   root.title("Maths Quiz Game")
   Start(root)
   root.mainloop()
