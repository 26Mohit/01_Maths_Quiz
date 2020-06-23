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
        selected_questions = 6
        levels = 1

        # retrieve selected range
        lowest = 0
        highest = 50

        Quiz(self, levels, selected_questions, lowest, highest)

        # hide start up window
        root.withdraw()


class Quiz:
    def __init__(self, partner, levels, selected_questions, lowest, highest):
        print(levels)
        print(selected_questions)
        print(lowest)
        print(highest)

        # initialise variables
        self.questions = IntVar()
        self.lowest = IntVar()
        self.highest = IntVar()

        # Set number of questions to amount entered by users at start of quiz
        self.questions.set(selected_questions)

        # Set range of numbers to values entered by users
        self.lowest.set(lowest)
        self.highest.set(highest)

        # GUI setup
        self.quiz_box = Toplevel()
        self.quiz_frame = Frame(self.quiz_box, padx=10, pady=10)
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

        self.answers_entry_frame = Frame(self.quiz_frame, width=200)
        self.answers_entry_frame.grid(row=2)

        # questions box
        self.questions_box = Label(self.answers_entry_frame, bg="#FFCCFF",
                                   font="Arial 24 bold", width=13, pady=10)
        self.questions_box.grid(row=0)

        # answers entry box
        self.answers_entry = Entry(self.answers_entry_frame,
                                        font="Arial 28 bold", width=13, justify=CENTER)
        self.answers_entry.grid(row=1)

        self.submit_button = Button(self.answers_entry_frame,
                                       font="Arial 20 bold",
                                       text="Submit", bg="#FFFF33", width=12)
        self.submit_button.grid(row=2, column=0)

        self.next_button = Button(self.answers_entry_frame,
                                       font="Arial 18 bold", width=7,
                                       text="Next→", bg="#00CC00", fg="white",
                                  command=self.generate_questions)
        self.next_button.grid(row=1, column=1)

        self.answers_error_label = Label(self.answers_entry_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.answers_error_label.grid(row=4, columnspan=2, pady=10)

        # Error Label goes here
        self.answers_error_label = Label(self.quiz_frame, fg="red", font="Arial 14 italic",
                                        text="", justify=CENTER)
        self.answers_error_label.grid(row=4)

        # selected questions Label (row 3)

        self.questions_label = Label(self.quiz_frame, text="Welcome, your selected number of questions: 30"
                                                           " and selected range of numbers: 0-50 ",
                                     font="Arial 12 bold",
                                     fg="green", wrap=400, justify=CENTER)
        self.questions_label.grid(row=3)

        # Help/Rules and quiz results button (row 4)
        self.buttons_frame = Frame(self.quiz_frame)
        self.buttons_frame.grid(row=4)

        self.results_button = Button(self.buttons_frame, text="Quiz Results...",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.results_button.grid(row=5, column=0, padx=2, pady=10)

        self.quit_button = Button(self.buttons_frame, text="End Quiz",
                                  font="Arial 15 bold",
                                  bg="#EA6B66", fg="white")
        self.quit_button.grid(row=5, column=1, padx=5, pady=5)

        self.help_button = Button(self.buttons_frame, text="How to Play?",
                                  font="Arial 15 bold", bg="#808080", fg="white")
        self.help_button.grid(row=5, column=2, padx=2, pady=10)

    def generate_questions(self):

        # retrieve the questions from the initial function..
        questions = self.questions.get()
        lowest = self.lowest.get()
        highest = self.highest.get()

        # adjust the questions
        questions -= 1
        problems = []

        import random
        # Generate number of questions that user has entered
        # Generate numbers according to the values entered by user
        # Generate questions according to the level user chose
        for selected_questions in range(questions):
            num_1 = random.randint(lowest, highest)
            num_2 = random.randint(lowest, highest)
            sign = ['+', '-', '*']
            levels = random.choice(sign)
            question = "{} {} {} = ".format(num_1, levels, num_2)
            correct = eval(str(num_1) + levels + str(num_2))
            answer = self.answers_entry

            problems.append(question)
            self.questions_box.configure(text="{}".format(question))


            if answer == correct:
                print("Great job")
            else:
                print(correct)
                print("oops")

        # Set questions to adjust questions
        self.questions.set(questions)

        # Edit label so user can see their questions
        self.questions_label.configure(text="questions: {}".format(questions))





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start(root)
    root.mainloop()
