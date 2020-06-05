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
        self.highest.set(10)

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
                                          wrap=500, justify=CENTER, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)

        # Range of numbers Label (row 5)
        self.range_label = Label(self.start_frame, font="Arial 10 italic bold",
                                     text="Please enter a range of numbers",
                                     wrap=275, justify=CENTER, padx=10, pady=10)
        self.range_label.grid(row=5)

        # range of numbers Entry Boxes, Button (row 6)
        self.range_entry_frame = Frame(self.start_frame, width=200)
        self.range_entry_frame.grid(row=6)

        self.lowest_label = Label(self.range_entry_frame, font="Arial 10 italic bold",
                                  text="Lowest", wrap=225, justify=LEFT)
        self.lowest_label.grid(row=0, column=0)

        self.lowest_entry = Entry(self.range_entry_frame,
                                        font="Arial 16 bold", width=7)
        self.lowest_entry.grid(row=0, column=1)

        self.lowest_error_label = Label(self.range_entry_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.lowest_error_label.grid(row=1, columnspan=2, pady=10)

        self.highest_label = Label(self.range_entry_frame,font="Arial 10 italic bold",
                                  text="Highest", wrap=225, justify=LEFT)
        self.highest_label.grid(row=0, column=2)

        self.highest_entry = Entry(self.range_entry_frame,
                                        font="Arial 16 bold", width=7)
        self.highest_entry.grid(row=0, column=3)

        self.highest_error_label = Label(self.range_entry_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.highest_error_label.grid(row=1, columnspan=2, pady=10)

        self.select_button = Button(self.range_entry_frame,
                                       font="Arial 12 bold",
                                       text="Select", bg="#FF9933",
                                       command=self.check_range)
        self.select_button.grid(row=0, column=4)

        # Error Label goes here
        self.range_error_label = Label(self.range_entry_frame, fg="red", font="Arial 10 italic",
                                        text="")
        self.range_error_label.grid(row=1, column=2)

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

        # Help Button
        self.help_button = Button(self.start_frame, text="How to play?",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=12, pady=10)

    def check_range(self):
        lowest = self.lowest_entry.get()
        highest = self.highest_entry.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white (for testing purposes)...
        self.lowest_entry.config(bg="white")
        self.highest_entry.config(bg="white")
        self.range_error_label.config(text="")

        # Disable all levels buttons in case user changes mind and
        # decreases amount entered.
        self.easy_level_button.config(state=DISABLED)
        self.medium_level_button.config(state=DISABLED)
        self.hard_level_button.config(state=DISABLED)

        try:

            lowest_entry = int(lowest)
            highest_entry = int(highest)


            if lowest_entry >= highest_entry:
                has_errors = "yes"
                error_feedback = "please, enter a lower value in the lowest box and" \
                                 " a higher value in the highest box."

            elif lowest_entry < 0:
                has_errors = "yes"
                error_feedback = "Please, choose numbers between 0-1000."

            elif highest_entry > 1000:
                has_errors = "yes"
                error_feedback = "Please, choose numbers between 0-1000."

            elif highest_entry - lowest_entry < 10:
                has_errors = "yes"
                error_feedback = "The range must contain at least 10 numbers."

            elif lowest_entry >= 100:
                # enable easy level button
                self.easy_level_button.config(state=NORMAL)

            elif highest_entry > 100:
                # enable easy level button
                self.easy_level_button.config(state=NORMAL)

            elif lowest_entry < 100:
                # enable easy and medium level buttons
                self.easy_level_button.config(state=NORMAL)
                self.medium_level_button.config(state=NORMAL)

            if lowest_entry >= highest_entry:
                has_errors = "yes"
                error_feedback = "please, enter a lower value in the lowest box and" \
                                 " a higher value in the highest box."

            elif lowest_entry < 0:
                has_errors = "yes"
                error_feedback = "Please, choose numbers between 0-1000."

            elif highest_entry > 1000:
                has_errors = "yes"
                error_feedback = "Please, choose numbers between 0-1000."

            elif highest_entry - lowest_entry < 10:
                has_errors = "yes"
                error_feedback = "The range must contain at least 10 numbers."

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number (no text / decimals)"

        if has_errors == "yes":
            self.lowest_entry.config(bg=error_back)
            self.highest_entry.config(bg=error_back)
            self.range_error_label.config(text=error_feedback)

        else:
            # set selected range to amounts entered by user
            self.lowest.set(lowest)
            self.highest.set(highest)

    def to_play(self, levels):

        # retrieve selected range
        lowest = self.lowest.get()
        highest = self.highest.get()

        Quiz(self, levels, lowest, highest)

        # hide start up window
        # root.withdraw()


class Quiz:
    def __init__(self, partner, levels, lowest, highest):
        print(levels)
        print(lowest)
        print(highest)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start(root)
    root.mainloop()
