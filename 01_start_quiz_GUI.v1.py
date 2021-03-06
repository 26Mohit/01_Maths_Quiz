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

        # Number of questions label (row 2)
        self.questions_label = Label(self.start_frame, font="Arial 10 bold",
                                     text="Please enter number of questions",
                                     wrap=400, justify=CENTER, padx=10, pady=10)
        self.questions_label.grid(row=2)

        # Number of questions entry box and button (row 3)
        self.questions_entry_frame = Frame(self.start_frame, width=200)
        self.questions_entry_frame.grid(row=3)

        self.questions_entry = Entry(self.questions_entry_frame,
                                        font="Arial 16 bold", width=15)
        self.questions_entry.grid(row=0, column=0)

        self.select_button = Button(self.questions_entry_frame,
                                       font="Arial 12 bold",
                                       text="Select", bg="#FF9933",
                                       command=self.check_inputs)
        self.select_button.grid(row=0, column=1)

        self.questions_error_label = Label(self.questions_entry_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.questions_error_label.grid(row=4, columnspan=2, pady=10)

        # Error Label goes here
        self.questions_error_label = Label(self.questions_entry_frame, fg="red", font="Arial 10 italic",
                                        text="", justify=CENTER)
        self.questions_error_label.grid(row=1)

        # Levels label (row 8)

        self.levels_label = Label(self.start_frame, font="Arial 16 bold",
                                  text="Choose your level",
                                  wrap=275, justify=CENTER)
        self.levels_label.grid(row=8)

        # buttons frame (row 9-11)
        self.levels_frame = Frame(self.start_frame)
        self.levels_frame.grid(row=9)

        # Buttons go here...
        button_font = "Arial 14 bold"
        # Blue Easy level button...
        self.easy_level_button = Button(self.levels_frame, text="Easy (+/-)",
                                        command=lambda: self.to_play(1),
                                        font=button_font, bg="#00CCCC",
                                        width=14, height=1)
        self.easy_level_button.grid(row=9, column=1, pady=10)

        # green medium level button...
        self.medium_level_button = Button(self.levels_frame, text="Medium (x/÷)",
                                           command=lambda: self.to_play(2),
                                           font=button_font, bg="#99FF33",
                                          width=14, height=1)
        self.medium_level_button.grid(row=10, column=1, padx=5, pady=10)

        # red hard level button...
        self.hard_level_button = Button(self.levels_frame, text="Hard (²/√)",
                                         command=lambda: self.to_play(3),
                                         font=button_font, bg="#E51400",
                                        width=14, height=1)
        self.hard_level_button.grid(row=11, column=1, pady=10)

        # Disable all levels buttons at start
        self.easy_level_button.config(state=DISABLED)
        self.medium_level_button.config(state=DISABLED)
        self.hard_level_button.config(state=DISABLED)

        # Help Button
        self.help_button = Button(self.start_frame, text="How to play",
                                  bg="#808080", fg="white", font=button_font, width=10, height=2)
        self.help_button.grid(row=12, column=0, pady=10)

    def check_inputs(self):
        selected_questions = self.questions_entry.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # change background to white (for testing purposes)...
        self.questions_entry.config(bg="white")
        self.questions_error_label.config(text="")

        # Disable all levels buttons in case user changes mind and
        # decreases amount entered.
        self.easy_level_button.config(state=DISABLED)
        self.medium_level_button.config(state=DISABLED)
        self.hard_level_button.config(state=DISABLED)

        try:
            selected_questions = int(selected_questions)

            if selected_questions < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you can play with is 5"
            elif selected_questions > 30:
                has_errors = "yes"
                error_feedback = "please choose a number between 5-30"

            elif selected_questions >= 5-30:
                # enable hard level button
                self.hard_level_button.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number (no text / decimals)"

        if has_errors == "yes":
            self.questions_entry.config(bg=error_back)
            self.questions_error_label.config(text=error_feedback)
        else:
            # set selected questions to number entered by user
            self.questions.set(selected_questions)

    def to_play(self, levels):

        # retrieve starting balance
        selected_questions = self.questions.get()

        Quiz(self, levels, selected_questions)

        # hide start up window
        # root.withdraw()


class Quiz:
    def __init__(self, partner, levels, selected_questions):
        print(levels)
        print(selected_questions)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start(root)
    root.mainloop()
