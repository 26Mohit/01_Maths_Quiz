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

        # Set Initial Lowest to zero
        self.lowest = IntVar()

        # Set Initial Highest to zero
        self.highest = IntVar()

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
                                               " For Medium and Hard Levels recommended range is 0-20."
                                               " Please choose a range of at least 10 numbers. ",
                                          wrap=550, justify=LEFT, padx=10, pady=10)
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

        self.enter_button = Button(self.questions_entry_frame,
                                       font="Arial 14 bold",
                                       text="Enter", bg="#FF9933",
                                       command=self.check_inputs)
        self.enter_button.grid(row=0, column=1)

        self.questions_error_label = Label(self.questions_entry_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.questions_error_label.grid(row=4, columnspan=2, pady=5)

        # Error Label goes here
        self.questions_error_label = Label(self.start_frame, fg="red", font="Arial 12 italic",
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

        self.select_button = Button(self.range_entry_frame,
                                       font="Arial 14 bold",
                                       text="Select", bg="#FF9933",
                                       command=self.check_range)
        self.select_button.grid(row=0, column=4)

        # Error Label goes here
        self.range_error_label = Label(self.start_frame, fg="red", font="Arial 12 italic",
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
                                        command=lambda:(self.to_play(1)),
                                        font=button_font, bg="#00CCCC",
                                        width=18, height=1)
        self.easy_level_button.grid(row=9, column=1, pady=10)

        # green medium level button...
        self.medium_level_button = Button(self.levels_frame, text="Medium (x/÷)",
                                          command=lambda:(self.to_play(2)),
                                           font=button_font, bg="#99FF33",
                                          width=18, height=1)
        self.medium_level_button.grid(row=10, column=1, padx=5, pady=10)

        # red hard level button...
        self.hard_level_button = Button(self.levels_frame, text="Hard (²/√)",
                                        command=lambda:(self.to_play(3)),
                                        font=button_font, bg="#ff3333",
                                        width=18, height=1)
        self.hard_level_button.grid(row=11, column=1, pady=10)

        # Disable all levels buttons at start
        self.easy_level_button.config(state=DISABLED)
        self.medium_level_button.config(state=DISABLED)
        self.hard_level_button.config(state=DISABLED)

        # Disable the select button before users enter the amount of questions
        self.select_button.config(state=DISABLED)

        # Help Button
        self.help_button = Button(self.start_frame, text="How to play?",
                                  bg="#808080", fg="white", command=lambda:(self.to_help()),
                                  font=button_font, width=15, height=2)
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


        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number (no text / decimals)"

        if has_errors == "yes":
            self.questions_entry.config(bg=error_back)
            self.questions_error_label.config(text=error_feedback)
        else:
            self.questions_entry.config(bg="#57FF5C")
            # enable select button
            self.select_button.config(state=NORMAL)
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


        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a whole number (no text / decimals)"

        if has_errors == "yes":
            self.lowest_entry.config(bg=error_back)
            self.highest_entry.config(bg=error_back)
            self.range_error_label.config(text=error_feedback)

        else:
            self.lowest_entry.config(bg="#57FF5C")
            self.highest_entry.config(bg="#57FF5C")
            # enable easy and medium level buttons
            self.easy_level_button.config(state=NORMAL)
            self.medium_level_button.config(state=NORMAL)
            self.hard_level_button.config(state=NORMAL)
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
        self.start_frame.destroy()

    def to_help(self):
        get_help = Help(self)


class Quiz:
    def __init__(self, partner, levels, selected_questions, lowest, highest):

        # initialise variables
        self.num_questions = IntVar()
        self.lowest = IntVar()
        self.highest = IntVar()
        self.correct = IntVar()
        self.score = IntVar()

        # Set number of questions to amount entered by users at start of quiz
        self.num_questions.set(selected_questions)

        # Set range of numbers to values entered by users
        self.lowest.set(lowest)
        self.highest.set(highest)

        # Get problems according to the mode chosen by users
        self.problems = IntVar()
        self.problems.set(levels)

        # list for holding results
        self.quiz_results_list = [selected_questions, selected_questions]
        self.round_results_list = []
        self.results = IntVar()

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
            self.Mode_label.config(text="Quiz (Easy Mode)", fg="#00CCCC")
        elif levels == 2:
            self.Mode_label.config(text="Quiz (Medium Mode)", fg="#00CC00")
        elif levels == 3:
            self.Mode_label.config(text="Quiz (Hard Mode)", fg="#ff3333")

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
                                    command=self.check_answers,
                                    bg="#FFFF33", width=12)
        self.submit_button.grid(row=2, column=0)
        self.submit_button.config(state=DISABLED)

        self.next_button = Button(self.answers_entry_frame,
                                       font="Arial 18 bold", width=7,command=self.generate_questions,
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
                                   command=lambda: self.to_results(self.round_results_list, self.quiz_results_list),
                                   bg="#003366", fg="white")
        self.results_button.grid(row=5, column=0, padx=2, pady=10)

        # Disable Results button
        self.results_button.config(state=DISABLED)

        self.quit_button = Button(self.buttons_frame, text="End Quiz",
                                  font="Arial 15 bold", command=self.to_end,
                                  bg="#EA6B66", fg="white")
        self.quit_button.grid(row=5, column=1, padx=5, pady=5)

        self.help_button = Button(self.buttons_frame, text="How to Play?",
                                  command=lambda:(self.to_help()),
                                  font="Arial 15 bold", bg="#808080", fg="white")
        self.help_button.grid(row=5, column=2, padx=2, pady=10)

    def generate_questions(self):

        # retrieve the questions from the initial function..
        questions = self.num_questions.get()
        lowest = self.lowest.get()
        highest = self.highest.get()
        problems_generator = self.problems.get()

        # adjust the questions
        questions -= 1

        # Generate number of questions that user has entered
        # Generate numbers according to the values entered by user
        # Generate questions according to the level user chose

        num_1 = random.randint(1, highest)
        num_2 = random.randint(lowest, highest)

        if problems_generator == 1:
            num_3 = num_1 + num_2
            sign = ['+', '-']
            level = random.choice(sign)
            question = "{} {} {} = ".format(num_3, level, num_2)
            var_correct = eval(str(num_3) + level + str(num_2))
            self.answers_entry.get()
            self.correct.set(var_correct)
            self.questions_box.configure(text="{}".format(question))
            round_results = "{} ".format(question)
            self.round_results_list.append(round_results)

        elif problems_generator == 2:
            num_3 = num_1*num_2
            sign = ['*', '/']

            level = random.choice(sign)
            if level == "*":
                display_sign = "×"
            else:
                display_sign = "÷"

            if level == '*':
                display_question = "{} {} {} = ".format(num_1, display_sign, num_2)
            else:
                display_question = "{} {} {} = ".format(num_3, display_sign, num_1)

            if display_sign == "×":
                question = "{} {} {}".format(num_1, level, num_2)
            else:
                question = "{} / {} ".format(num_3, num_1)

            var_correct = eval(question)
            var_correct = int(var_correct)
            var_correct = str(var_correct)
            self.correct.set(var_correct)
            self.answers_entry.get()
            self.questions_box.configure(text="{}".format(display_question))
            round_results = "{}".format(display_question)
            self.round_results_list.append(round_results)

        elif problems_generator == 3:

            num_3 = (num_1*num_1)
            sign = ['**2', '**1/2']
            level = random.choice(sign)
            if level == "**2":
                display_sign = "²"
            else:
                display_sign = "√"
            if level == "**2":
                display_question = "{} {} ".format(num_1, display_sign)
            else:
                display_question = "{} {} ".format(display_sign, num_3)

            if display_sign == "²":
                question = "{} {} ".format(num_1, level)
            else:
                question = "{} **.5".format(num_3)

            var_correct = eval(question)
            var_correct = int(var_correct)
            var_correct = str(var_correct)
            self.answers_entry.get()
            self.correct.set(var_correct)
            self.questions_box.configure(text="{}".format(display_question))
            round_results = "{}".format(display_question)
            self.round_results_list.append(round_results)

        self.next_button.config(state=DISABLED)
        self.answers_entry.config(bg="white")
        self.answers_entry.delete(0, END)
        self.submit_button.config(state=NORMAL)

        self.questions_label.configure(text="Questions: {}".format(questions))

        # Set questions to adjust questions
        self.num_questions.set(questions)

    def check_answers(self):
        questions = self.num_questions.get()
        # adjust the score
        score = self.score.get()

        var_correct = self.correct.get()
        answer = self.answers_entry.get()
        # check answers
        if answer == str(var_correct):
            score = score + 1
            self.answers_entry.config(bg="#57FF5C")
            self.questions_label.config(text="Correct, Well Done\n"
                                             "Score: {}\n".format(score), )
            round_results = "Correct | You entered:{} | Score:{}\n".format(answer, score)
            self.round_results_list.append(round_results)

        else:
            self.answers_entry.config(bg="#ffafaf")
            self.questions_label.config(text="Sorry, the answer is Incorrect\n"
                                             "The correct answer is:{}\n"
                                             "Score: {}\n".format(var_correct, score))
            round_results = "Incorrect |the correct answer is:{} | You entered:{} | Score:{}\n"\
                            .format(var_correct, answer, score)
            self.round_results_list.append(round_results)

        self.submit_button.config(state=DISABLED)
        self.next_button.config(state=NORMAL)
        self.score.set(score)

        self.quiz_results_list[0] = score
        selected_questions = self.quiz_results_list[1]

        if questions == 0:
            self.results_button.config(state=NORMAL)
            self.next_button.config(state=DISABLED)
            self.submit_button.config(text="Quiz Ended")
            if selected_questions - score == 0:
                self.questions_label.config(text="Congratulation, you have successfully accomplished"
                                                 " the quiz with a 100% score, thanks for playing. \n"
                                                 "your final score is {}/{}\n".format(score, selected_questions))
            if 0 < (selected_questions - score) <= selected_questions/2:
                self.questions_label.config(text="Good Job, you have successfully accomplished the quiz with a score above average"
                                                 ", thanks for playing. \n"
                                                 "your final score is {}/{}\n".format(score, selected_questions), fg="#ff9933")
            if selected_questions - score >= selected_questions/2:
                self.questions_label.config(text="Well played, but try to achieve better score next time, thanks for playing.\n"
                                                 "your final score is {}/{}\n".format(score,selected_questions), fg="#ffcc00")
            if selected_questions - score == selected_questions:
                self.questions_label.config(text="Sorry, you failed to accomplished the quiz, work hard on these questions"
                                                 " and try better next time, thanks for playing.\n"
                                                 "your final score is {}/{}\n".format(score, selected_questions), fg="#ff0000")

    def to_end(self):
        root.destroy()

    def to_help(self):
        get_help = Help(self)

    def to_results(self, quiz_history, quiz_results):
        QuizResults(self, quiz_history, quiz_results)


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


class QuizResults:
    def __init__(self, partner, quiz_history, quiz_results):

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
                                         text="Here are your quiz results.\n"
                                              "Please use the "
                                              "Export button to access the results "
                                              "of each round that you played ",
                                         wrap=300,
                                         font="arial 10 italic",
                                         justify=CENTER, width=40, fg="green",
                                         padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Selected Questions (row 2)
        self.details_frame = Frame(self.results_frame)
        self.details_frame.grid(row=2)

        # Score (row 2.0)
        self.score_label = Label(self.details_frame, font=heading, text="Score:", anchor="e")
        self.score_label.grid(row=0, column=0, padx=0)

        self.score_label = Label(self.details_frame, font=content, text="{}/{}"
                                 .format(quiz_results[0], quiz_results[1]), anchor="w")
        self.score_label.grid(row=0, column=1, padx=0)

        # Correct answers (row 2.1)
        self.correct_ans_label = Label(self.details_frame, font=heading,
                                       text="Correct Answers:", anchor="e")
        self.correct_ans_label.grid(row=1, column=0, padx=0)

        self.correct_ans_label = Label(self.details_frame, font=content,
                                       text="{}"
                                       .format(quiz_results[0]), fg="#00CC00", anchor="w")
        self.correct_ans_label.grid(row=1, column=1, padx=0)

        # Wrong Answers (row 2.2)
        self.wrong_ans_label = Label(self.details_frame, font=heading,
                                     text="Wrong Answers: ", anchor="e")
        self.wrong_ans_label.grid(row=3, column=0, padx=0)

        self.wrong_ans_label = Label(self.details_frame, font=content,
                                     text="{}"
                                     .format(quiz_results[1] - quiz_results[0]), fg="#ff3333", anchor="w")
        self.wrong_ans_label.grid(row=3, column=1, padx=0)

        # Percentage (row 2.3)
        self.percentage_label = Label(self.details_frame, font=heading,
                                      text="Percentage: ", anchor="e")
        self.percentage_label.grid(row=4, column=0, padx=0)

        self.percentage_label = Label(self.details_frame, font=content,
                                      text=" {:.1f}%"
                                      .format(quiz_results[0] / quiz_results[1]*100), anchor="w")
        self.percentage_label.grid(row=4, column=1, padx=0)

        # Dismiss button (row 3)
        self.dismiss_button = Button(self.details_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     width=10, bg="#EA6B66", fg="white",
                                     command=partial(self.close_results, partner))
        self.dismiss_button.grid(row=5, column=1, pady=10)

        all_quiz_results = ["Score: {}/{}\n"
                            "Correct answers:{}\n"
                            "Wrong answers:{}\n"
                            "Percentage:{:.1f}%".format(quiz_results[0], quiz_results[1],
                                                    quiz_results[0],
                                                    (quiz_results[1]-quiz_results[0]),
                                                    (quiz_results[0] / quiz_results[1]*100))]

        # Export Button
        self.export_button = Button(self.details_frame, text="Export...",
                                    font="Arial 12 bold", fg="white", bg="#003366", width="10"
                                    , command=lambda: self.export(partner, quiz_history, all_quiz_results))
        self.export_button.grid(row=5, column=0, pady=10)

    def close_results(self, partner):
        # Put stats back to normal...
        partner.results_button.config(state=NORMAL)
        self.results_box.destroy()

    def export(self, partner, quiz_history, all_quiz_results):
        Export(self, quiz_history, all_quiz_results)


class Export:
    def __init__(self, partner, quiz_history, all_quiz_results):

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (i.e: export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # Set up export heading (row)
        self.how_heading = Label(self.export_frame, text="Export / Instruction",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        # Export Instruction (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "and press the Save "
                                                         "button to save your "
                                                         "calculation history "
                                                         "to a text file ",
                                 justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # warning text(label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                                         "you enter below "
                                                         "already exists, "
                                                         " its contents will "
                                                         "be replaced with "
                                                         "your calculation "
                                                         "history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4)

        # Save / cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save", font="Arial 15 bold",
                                  bg="#003366", fg="white",
                                  command=partial(lambda: self.save_history(partner, quiz_history, all_quiz_results)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", font="Arial 15 bold",
                                  bg="#EA6B66", fg="white",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, quiz_history, quiz_results):

        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no space allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # Heading for stats
            f.write("Quiz Results\n\n")

            # Game Stats
            for rounds in quiz_results:
                f.write(rounds + "\n")


            # Heading for Rounds
            f.write("\nRound Details\n\n")

            # add new line at end of each item
            for item in quiz_history:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start(root)
    root.mainloop()
