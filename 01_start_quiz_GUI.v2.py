from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to select number of question, range of numbers and a level
        self.start_frame = Frame(padx=10, pady=10)
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
                                          wrap=400, justify=LEFT, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)

        # Range of numbers Label (row 5)
        self.range_label = Label(self.start_frame, font="Arial 10 italic bold",
                                     text="Please enter a range of numbers",
                                     wrap=275, justify=CENTER, padx=10, pady=10)
        self.range_label.grid(row=5)

        # range of numbers Entry Box, Button (row 6)
        self.range_entry_frame = Frame(self.start_frame, width=200)
        self.range_entry_frame.grid(row=6)

        self.range_entry = Entry(self.range_entry_frame,
                                        font="Arial 16 bold", width=10)
        self.range_entry.grid(row=0, column=0)

        self.select_button = Button(self.range_entry_frame,
                                       font="Arial 14 bold",
                                       text="Select",
                                       command=self.check_inputs)
        self.select_button.grid(row=0, column=1)

        self.range_error_label = Label(self.range_entry_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.range_error_label.grid(row=1, columnspan=2, pady=5)

        # Levels label (row 8)
        
        self.levels_label = Label(self.start_frame, font="Arial 14",
                                  text="Choose your level",
                                  wrap=275, justify=CENTER)
        self.levels_label.grid(row=8)

        # buttons frame (row 9-11)
        self.levels_frame = Frame(self.start_frame)
        self.levels_frame.grid(row=9)

        # Buttons go here...
        button_font = "Arial 12 bold"
        # Blue Easy level button...
        self.easy_level_button = Button(self.levels_frame, text="Easy (+/-)",
                                        command=lambda: self.to_play(1),
                                        font=button_font, bg="#00CCCC")
        self.easy_level_button.grid(row=9, column=1, pady=10)

        # green medium level button...
        self.medium_level_button = Button(self.levels_frame, text="Medium (x/÷)",
                                           command=lambda: self.to_play(2),
                                           font=button_font, bg="#00CC00")
        self.medium_level_button.grid(row=10, column=1, padx=5, pady=10)

        # red hard level button...
        self.hard_level_button = Button(self.levels_frame, text="Hard (²/√)",
                                         command=lambda: self.to_play(3),
                                         font=button_font, bg="#E51400")
        self.hard_level_button.grid(row=11, column=1, pady=10)

        # Disable all levels buttons at start
        self.easy_level_button.config(state=DISABLED)
        self.medium_level_button.config(state=DISABLED)
        self.hard_level_button.config(state=DISABLED)

        # Error Label goes here
        self.range_error_label = Label(self.start_frame, fg="red", font="Arial 12 italic",
                                        text="")
        self.range_error_label.grid(row=4)

        # Help Button
        self.help_button = Button(self.start_frame, text="How to play?",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=12, pady=10)

    def check_inputs(self):
        selected_range = self.range_entry.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white (for testing purposes)...
        self.range_entry.config(bg="white")
        self.range_error_label.config(text="")

        # Disable all levels buttons in case user changes mind and
        # decreases amount entered.
        self.easy_level_button.config(state=DISABLED)
        self.medium_level_button.config(state=DISABLED)
        self.hard_level_button.config(state=DISABLED)

        try:
            selected_range = int(selected_range)

            if selected_range < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you can play with is $5"
            elif selected_range > 50:
                has_errors = "yes"
                error_feedback = "Too high! The most you can risk in " \
                                 "this game is $50"

            elif selected_range >= 15:
                # enable all buttons
                self.easy_level_button.config(state=NORMAL)
                self.medium_level_button.config(state=NORMAL)
                self.hard_level_button.config(state=NORMAL)
            elif selected_range >= 10:
                # enable low and medium levels buttons
                self.easy_level_button.config(state=NORMAL)
                self.medium_level_button.config(state=NORMAL)
            else:
                self.easy_level_button.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimals)"

        if has_errors == "yes":
            self.range_entry.config(bg=error_back)
            self.range_error_label.config(text=error_feedback)
        else:
            # set starting balance to amount entered by user
            self.questions.set(selected_range)

    def to_play(self, levels):

        # retrieve starting balance
        selected_range = self.questions.get()

        Quiz(self, levels, selected_range)

        # hide start up window
        # root.withdraw()
        
class Quiz:
    def __init__(self, partner, levels, selected_range):
        print(levels)
        print(selected_range)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start(root)
    root.mainloop()
