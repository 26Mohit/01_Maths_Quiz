
from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Start:
    def __init__(self, parent):

        # start Main screen GUI...
        self.start_frame = Frame(width=600, height=600)
        self.start_frame.grid()

        # Mystery Box Heading (row 0)
        self.start_label = Label(self.start_frame, text="Maths Quiz",
                                      font="Arial 16 bold",
                                      padx=10, pady=10)
        self.start_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.start_frame, text="Help", padx=10, pady=10,
                                  command=self.to_help)
        self.help_button.grid(row=1, pady=10)

    def to_help(self):
        get_help = Help(self)


class Help:
    def __init__(self,partner):

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (i.e: help box)
        self.help_box = Toplevel()

        # if users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box)
        self.help_frame.grid()

        # Set up Help heading (row)
        self.how_heading = Label(self.help_frame,text="How To Play",
                                 font="arial 16 bold")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="To Play a quiz\n"
                                                     "First, choose the number of questions between the given range and \n"
                                                     "then choose the range of numbers according to the level you want to play.\n" 
                                                     "After that select a level to start the quiz.\n"
                                                     "Quiz Modes\n"
                                                     "The Easy mode will have questions on Addition(+) and Subtraction(-).\n"
                                                     "The Medium mode will have questions on Multiplication(x) and Division(÷).\n"
                                                     "The Hard mode will have questions on Square(2) and Square root(√).\n"
                                                     "Quiz Rules\n"
                                                     "Enter an answer in the given space and \n"
                                                     "then click the 'Submit' button to lock your answer and \n"
                                                     "as you do that there some feedback will appear about your answer.\n"
                                                     "Click the 'Next' button to see the other questions.\n"
                                                     "Quiz Results\n"
                                                     "To see your results go to the 'Quiz Result' and \n"
                                                     "to save your progress click the 'Export' button and \n"
                                                     "then enter a valid file name and click the 'Save' button.\n",
                               width=60, wrap=500, justify=LEFT, font="arial 10")
        self.help_text.grid(row=1)

        # Dismiss button ( row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", font="Arial 15 bold",
                                  width=15, bg="#EA6B66", fg="white",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start(root)
    root.mainloop()
