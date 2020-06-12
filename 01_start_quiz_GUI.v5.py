from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to select number of question, range of numbers and a level
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Set Initial questions to zero
        self.questions_amount = IntVar()
        self.questions_amount.set(0)

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
        self.quiz_instructions = Label(self.start_frame, font="Arial 11 italic",
                                          text="Welcome, test your mathematical skills."
                                               " Before selecting a level, "
                                               "please enter the number of question between (5-30)"
                                               " you would like to have in your quiz."
                                               " Then please enter the range of numbers between 0-1000"
                                               " you would like to see in your quiz. "
                                               "please choose a range of at least 10 numbers. ",
                                          wrap=500, justify=LEFT, padx=10, pady=10)
        self.quiz_instructions.grid(row=1)

        # Number of questions label (row 2)
        self.questions_label = Label(self.start_frame, font="Arial 14 bold italic",
                                     text="Please enter number of questions",
                                     wrap=400, justify=CENTER, padx=10, pady=10)
        self.questions_label.grid(row=2)

        # Number of questions entry box and button (row 3)
        self.questions_entry_frame = Frame(self.start_frame, width=200,
                                           padx=5, pady=5)
        self.questions_entry_frame.grid(row=3)

        self.questions_entry = Entry(self.questions_entry_frame,
                                        font="Arial 22 bold", width=15)
        self.questions_entry.grid(row=0)

        self.questions_error_label = Label(self.questions_entry_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.questions_error_label.grid(row=4, columnspan=2, pady=5)

        # Error Label goes here
        self.questions_error_label = Label(self.start_frame, fg="red", font="Arial 14 italic",
                                        text="", justify=CENTER, wrap=400)
        self.questions_error_label.grid(row=4)

        # Range of numbers Label (row 5)
        self.range_label = Label(self.start_frame, font="Arial 14 italic bold",
                                     text="Please enter a range of numbers",
                                     wrap=500, justify=CENTER, padx=10, pady=10)
        self.range_label.grid(row=5)

        # range of numbers Entry Boxes, Button (row 6)
        self.range_entry_frame = Frame(self.start_frame, width=200)
        self.range_entry_frame.grid(row=6)

        self.lowest_label = Label(self.range_entry_frame, font="Arial 10 italic bold",
                                  text="Lowest", wrap=225, justify=LEFT)
        self.lowest_label.grid(row=0, column=0)

        self.lowest_entry = Entry(self.range_entry_frame,
                                        font="Arial 22 bold", width=7)
        self.lowest_entry.grid(row=0, column=1)

        self.lowest_error_label = Label(self.range_entry_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.lowest_error_label.grid(row=1, columnspan=2, pady=5)

        self.highest_label = Label(self.range_entry_frame,font="Arial 10 italic bold",
                                  text="Highest", wrap=225, justify=LEFT)
        self.highest_label.grid(row=0, column=2)

        self.highest_entry = Entry(self.range_entry_frame,
                                        font="Arial 22 bold", width=7)
        self.highest_entry.grid(row=0, column=3)

        self.highest_error_label = Label(self.range_entry_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.highest_error_label.grid(row=1, columnspan=2, pady=5)

        # Error Label goes here
        self.range_error_label = Label(self.start_frame, fg="red", font="Arial 14 italic",
                                        text="", wrap=400)
        self.range_error_label.grid(row=7)

        # Levels label (row 8)

        self.levels_label = Label(self.start_frame, font="Arial 16 bold",
                                  text="Choose your level",
                                  wrap=275, justify=CENTER)
        self.levels_label.grid(row=8)

        # buttons frame (row 9-11)
        self.levels_frame = Frame(self.start_frame)
        self.levels_frame.grid(row=9)

        # Buttons go here...
        button_font = "Arial 16 bold"
        # Blue Easy level button...
        self.easy_level_button = Button(self.levels_frame, text="Easy (+/-)",
                                        command=lambda:(self.to_play(1),
                                                        self.check_inputs(),
                                                        self.check_range()),
                                        font=button_font, bg="#00CCCC",
                                        width=18, height=1)
        self.easy_level_button.grid(row=9, column=1, pady=10)

        # green medium level button...
        self.medium_level_button = Button(self.levels_frame, text="Medium (x/÷)",
                                          command=lambda:(self.to_play(2),
                                                          self.check_inputs(),
                                                          self.check_range()),
                                           font=button_font, bg="#99FF33",
                                          width=18, height=1)
        self.medium_level_button.grid(row=10, column=1, padx=5, pady=10)

        # red hard level button...
        self.hard_level_button = Button(self.levels_frame, text="Hard (²/√)",
                                        command=lambda:(self.to_play(3),
                                                        self.check_inputs(),
                                                        self.check_range()),
                                        font=button_font, bg="#ff3333",
                                        width=18, height=1)
        self.hard_level_button.grid(row=11, column=1, pady=10)

        # Help Button
        self.help_button = Button(self.start_frame, text="How to play?",
                                  bg="#808080", fg="white", font=button_font, width=15, height=2)
        self.help_button.grid(row=12, column=0, pady=5)

    def check_inputs(self):
        selected_questions = self.questions_entry.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white (for testing purposes)...
        self.questions_entry.config(bg="white")
        self.questions_error_label.config(text="")

        try:
            selected_questions = int(selected_questions)

            if selected_questions < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you can play with is 5"
            elif selected_questions > 30:
                has_errors = "yes"
                error_feedback = "please choose a number between 5-30"

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number (no text / decimals)"

        if has_errors == "yes":
            self.questions_entry.config(bg=error_back)
            self.questions_error_label.config(text=error_feedback)
        else:
            # set selected questions to number entered by user
            self.questions_amount.set(selected_questions)

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

        # retrieve selected questions
        selected_questions = self.questions_amount.get()

        # retrieve selected range
        lowest = self.lowest.get()
        highest = self.highest.get()

        Quiz(self, levels, selected_questions, lowest, highest)

        # hide start up window
        # root.withdraw()


class Quiz:
    def __init__(self, partner, levels, selected_questions, lowest, highest):
        print(levels)
        print(selected_questions)
        print(lowest)
        print(highest)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start(root)
    root.mainloop()
