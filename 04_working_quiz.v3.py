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
        selected_questions = 10
        levels = 1

        # retrieve selected range
        lowest = 1
        highest = 12

        Quiz(self, levels, selected_questions, lowest, highest)

        # hide start up window
        root.withdraw()


class Quiz:
    def __init__(self, partner, levels, selected_questions, lowest, highest):
        print(levels)
        print(selected_questions)
        print(lowest)
        print(highest)

        self.correct = IntVar()



        # initialise variables
        self.num_questions = IntVar()
        self.lowest = IntVar()
        self.highest = IntVar()

        # Set number of questions to amount entered by users at start of quiz
        self.num_questions.set(selected_questions)

        # Set range of numbers to values entered by users
        self.lowest.set(lowest)
        self.highest.set(highest)

        # Get problems according to the mode chosen by users
        self.problems = IntVar()
        self.problems.set(levels)

        # GUI setup
        self.quiz_box = Toplevel()
        self.quiz_frame = Frame(self.quiz_box, padx=10, pady=10)
        self.quiz_frame.grid()

        # Mode row 0
        self.Mode_label = Label(self.quiz_frame,
                                font="Arial 24 bold", padx=10,
                                pady=10)
        self.Mode_label.grid(row=0)
        if levels == 1:
            self.Mode_label.config(text="Quiz (Easy Mode)")
        elif levels == 2:
            self.Mode_label.config(text="Quiz (Medium Mode)")
        elif levels == 3:
            self.Mode_label.config(text="Quiz (Hard Mode)")

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
                                       text="Submit",
                                    command=self.generate_questions,
                                    bg="#FFFF33", width=12)
        self.submit_button.grid(row=2, column=0)

        self.next_button = Button(self.answers_entry_frame,
                                       font="Arial 18 bold", width=7,command=self.Check,
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

        # selected questions Label (row 3)

        self.questions_label = Label(self.quiz_frame, text="Welcome, your selected number of questions: {}"
                                                           " and selected range of numbers: {}-{} ".format(selected_questions, lowest,
                                                                                                           highest),
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
        questions = self.num_questions.get()
        lowest = self.lowest.get()
        highest = self.highest.get()
        problems_generator = self.problems.get()

        # adjust the questions
        score = 0
        questions -= 1
        problems = []


        # Generate number of questions that user has entered
        # Generate numbers according to the values entered by user
        # Generate questions according to the level user chose

        num_1 = random.randint(lowest, highest)
        num_2 = random.randint(lowest, highest)


        if problems_generator == 1:
            num_3 = num_1 + num_2
            sign = ['+', '-']
            level = random.choice(sign)
            question = "{} {} {} = ".format(num_3, level, num_2)
            var_correct = eval(str(num_3) + level + str(num_2))
            answer = self.answers_entry.get()
            self.correct.set(var_correct)
            print("Correct answer set as...", var_correct)
            self.questions_box.configure(text="{}".format(question))


        # Set questions to adjust questions
        self.num_questions.set(questions)

        if questions == 0:
            self.submit_button.config(state=DISABLED)
            self.submit_button.config(text="Quiz Ended")

    def Check(self):
        var_correct = self.correct.get()
        print("Correct vairable received..", var_correct)
        answer = self.answers_entry.get()
        # check answers
        if answer == str(var_correct):
            print("great")
            print(answer)
        else:
            print("wrong")
            print(var_correct)
            print(answer)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start(root)
    root.mainloop()
