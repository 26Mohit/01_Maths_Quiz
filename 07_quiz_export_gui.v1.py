from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Quiz:
    def __init__(self):
        # Formatting variables...
        self.quiz_results_list = [4, 6]

        # In actual program this is blank and is populated with user calculation
        self.round_results_list = ['5 ÷ 5 = | correct | you entered:1 | score:1\n'
                                    '2 × 12 = | correct | you entered:24 | score:2\n'
                                    '2 × 7 = | incorrect | you entered:15 | the correct answer:14 | score:2\n'
                                    '9 × 7 = | correct | you entered:63 | score:3\n'
                                    '7 × 2 = | correct | you entered:14 | score:4\n'
                                    '4 × 7 = | incorrect | you entered:12 | the correct answer:28 | score:4']


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
                                       .format(quiz_results[0]), anchor="w")
        self.correct_ans_label.grid(row=1, column=1, padx=0)

        # Wrong Answers (row 2.2)
        self.wrong_ans_label = Label(self.details_frame, font=heading,
                                     text="Wrong Answers: ", anchor="e")
        self.wrong_ans_label.grid(row=3, column=0, padx=0)

        self.wrong_ans_label = Label(self.details_frame, font=content,
                                     text="{}"
                                     .format(quiz_results[1] - quiz_results[0]), anchor="w")
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
                                     width=10, bg="#660000", fg="white",
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
        print(all_quiz_results)
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
                                  bg="#660000", fg="white",
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



# main routine:
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    something = Quiz()
    root.mainloop()
