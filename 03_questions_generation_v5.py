import random

# Generate number of questions that user has entered
# Generate numbers according to the values entered by user
# Generate questions according to the level user chose
selected_questions = int(input("please enter number of questions:"))
lowest = int(input("please enter a low number"))
highest = int(input("please enter a high number"))
for selected_questions in range(selected_questions):
    range = lowest-highest
    num_1 = random.randint(lowest, highest)
    question = "{}² = ".format(num_1)
    correct = (num_1**2)
    answer = int(input(question))
    if answer == correct:
      print("Great job")
    else:
      print("oops")
      print(correct)

